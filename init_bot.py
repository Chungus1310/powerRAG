import os
from pdf_processor import process_pdf_and_create_embeddings

def initialize_environment():
    # Let's set up everything we need to get this bot running!
    print("Initializing business Discord bot environment...")
    
    # Making sure we have a place for our API keys
    if not os.path.exists(".env"):
        print("Creating .env file template...")
        with open(".env", "w") as f:
            f.write("# Discord Bot Token\n")
            f.write("DISCORD_TOKEN=your_discord_token_here\n\n")
            f.write("# Gemini API Key\n")
            f.write("GEMINI_API_KEY=your_gemini_api_key_here\n")
        print("Please fill in your API keys in the .env file")
    else:
        print(".env file already exists")
    
    # Looking for our business info file
    if os.path.exists("data.pdf"):
        print("Found data.pdf, processing...")
        process_pdf_and_create_embeddings("data.pdf")
    else:
        print("ERROR: data.pdf not found. Please place your business information PDF file in the root directory.")

if __name__ == "__main__":
    initialize_environment()