import os
from typing import List, Dict, Any
import chromadb
from chromadb.config import Settings
from google import genai
from google.genai import types
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get Gemini API key from environment variables
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

# Initialize the Google Genai client
client = genai.Client(api_key=GEMINI_API_KEY)

def generate_query_embedding(query: str) -> List[float]:
    # Convert user's question into AI-friendly format
    result = client.models.embed_content(
        model="models/text-embedding-004",
        contents=query,
        config=types.EmbedContentConfig(task_type="RETRIEVAL_QUERY")
    )
    
    return result.embeddings[0].values

def retrieve_relevant_chunks(query_embedding: List[float], top_k: int = 3) -> List[Dict[str, Any]]:
    # Find the most relevant info from our database
    chroma_client = chromadb.PersistentClient(path="./chroma_db")

    try:
        collection = chroma_client.get_collection(name="business_data")
    except Exception as e:
        raise ValueError(f"ChromaDB collection not found or path incorrect. Make sure to process the PDF first: {str(e)}")

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    relevant_chunks = []
    for i, doc in enumerate(results['documents'][0]):
        relevant_chunks.append({
            'text': doc,
            'score': results['distances'][0][i] if 'distances' in results else None
        })

    return relevant_chunks

def generate_response(query: str, relevant_chunks: List[Dict[str, Any]]) -> str:
    # Let Gemini work its magic to answer the question
    context = "\n\n".join([chunk['text'] for chunk in relevant_chunks])
    
    prompt = f"""
    Based on the following information about the business, please answer the user's question.
    
    Context information:
    {context}
    
    User's question: {query}
    
    Answer:
    """
    
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        config=types.GenerateContentConfig(
            system_instruction="""You are a business assistant bot that provides information strictly about the business 
            based on the given context. Only answer what can be inferred from the context.
            If the question can't be answered based on the context, politely state that you don't have that information.
            Be concise, professional, and helpful. Format your responses appropriately for Discord.""",
            temperature=0.2,
            top_k=40,
            top_p=0.95,
            max_output_tokens=800,
        ),
        contents=prompt
    )
    
    return response.text

def search_and_generate_response(query: str) -> str:
    # Main function that handles the whole Q&A process
    try:
        query_embedding = generate_query_embedding(query)
        relevant_chunks = retrieve_relevant_chunks(query_embedding)
        response = generate_response(query, relevant_chunks)
        
        return response
    except Exception as e:
        print(f"Error in RAG system: {str(e)}")
        return f"Sorry, I encountered an error while processing your question: {str(e)}"