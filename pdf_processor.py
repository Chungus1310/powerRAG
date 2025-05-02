import os
from typing import List, Dict
import PyPDF2
from langchain_text_splitters import RecursiveCharacterTextSplitter
from google import genai
from google.genai import types
import chromadb
from chromadb.config import Settings
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Google Genai client
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

# Initialize the Google Genai client
client = genai.Client(api_key=GEMINI_API_KEY)

def extract_text_from_pdf(pdf_path: str) -> str:
    # Pull all the text out of our PDF file
    text = ""
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def split_text_into_chunks(text: str, chunk_size: int = 1000, chunk_overlap: int = 200) -> List[str]:
    # Break down our text into bite-sized pieces
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len,
    )
    return text_splitter.split_text(text)

def generate_embeddings(chunks: List[str]) -> List[List[float]]:
    # Turn our text chunks into numbers that AI can understand
    embeddings = []
    batch_size = 5
    
    for i in range(0, len(chunks), batch_size):
        batch = chunks[i:i+batch_size]
        
        results = client.models.embed_content(
            model="models/text-embedding-004",
            contents=batch,
            config=types.EmbedContentConfig(task_type="RETRIEVAL_DOCUMENT")
        )
        
        for result in results.embeddings:
            embeddings.append(result.values)
            
    return embeddings

def store_embeddings_in_chromadb(chunks: List[str], embeddings: List[List[float]]) -> None:
    # Save everything in our database so we can find it later
    chroma_client = chromadb.PersistentClient(path="./chroma_db")
    collection = chroma_client.get_or_create_collection(name="business_data")
    ids = [f"doc_{i}" for i in range(len(chunks))]

    collection.add(
        embeddings=embeddings,
        documents=chunks,
        ids=ids
    )

    print(f"Successfully stored {len(chunks)} chunks in ChromaDB at ./chroma_db")

def process_pdf_and_create_embeddings(pdf_path: str = "data.pdf") -> None:
    # Main function that processes our PDF file
    print(f"Processing PDF: {pdf_path}")
    
    text = extract_text_from_pdf(pdf_path)
    print(f"Extracted {len(text)} characters from PDF.")
    
    chunks = split_text_into_chunks(text)
    print(f"Split into {len(chunks)} chunks.")
    
    print("Generating embeddings...")
    embeddings = generate_embeddings(chunks)
    
    store_embeddings_in_chromadb(chunks, embeddings)
    
    print("PDF processing and embedding creation complete!")

if __name__ == "__main__":
    process_pdf_and_create_embeddings()