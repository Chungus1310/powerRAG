# 🚀 PowerRAG: Your Business Discord Bot

## 🌟 Welcome to PowerRAG!

Hey there! Thanks for checking out **PowerRAG** - your friendly neighborhood Discord bot that turns your business documents into an interactive knowledge base. Powered by Gemini 2.0 and RAG (Retrieval-Augmented Generation) technology, this bot makes accessing your business information as easy as chatting with a friend.

Created with 💜 by [Chungus1310](https://github.com/Chungus1310)

## 🤔 What Does PowerRAG Do?

PowerRAG transforms your business PDFs into a smart Discord bot that can:

- Answer questions about your business using information from your documents
- Provide accurate, context-aware responses using Google's Gemini 2.0
- Make your business information accessible 24/7 through Discord

No more digging through files or scrolling through long documents - just ask and get answers!

## 🛠️ How It Works

Behind the scenes, PowerRAG uses some pretty cool tech:

1. **PDF Processing**: Extracts text from your business PDFs
2. **Text Chunking**: Breaks down the text into manageable pieces
3. **Embedding Generation**: Converts text into AI-friendly number sequences using Google's text-embedding-004 model
4. **Vector Database**: Stores everything in ChromaDB for lightning-fast retrieval
5. **RAG System**: Finds the most relevant information and generates human-like responses using Gemini 2.0

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- Discord account and a server where you're an admin
- Google AI Platform account (for Gemini API access)

### Installation

1. **Clone this repository**
   ```bash
   git clone https://github.com/Chungus1310/powerRAG.git
   cd powerRAG
   ```

2. **Install required packages**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your environment**
   ```bash
   python init_bot.py
   ```
   This will create a `.env` file template for you to fill in.

4. **Add your credentials**
   Open the `.env` file and add:
   - Your Discord bot token
   - Your Gemini API key

5. **Add your business information**
   Place your business information PDF in the root directory and name it `data.pdf`

6. **Process your PDF**
   ```bash
   python pdf_processor.py
   ```

7. **Launch your bot**
   ```bash
   python main.py
   ```

## 💬 Using PowerRAG

Once your bot is up and running, you can start asking questions in your Discord server:

```
!ask What are our business hours?
!ask What's our return policy?
!ask Who should I contact for technical support?
```

The bot will search through your documents and provide the most relevant information!

## 🔧 Customization

Want to tweak PowerRAG to better fit your needs? Here are some ways you can customize it:

- **Change the command prefix**: Edit the `command_prefix` in `main.py` to use something other than `!`
- **Adjust chunk size**: Modify the `chunk_size` and `chunk_overlap` parameters in `pdf_processor.py` to optimize for your specific documents
- **Customize response style**: Edit the system instruction in `rag_system.py` to change the bot's tone or formatting

## 🧩 Project Structure

- `init_bot.py`: Sets up the environment and checks for necessary files
- `main.py`: Contains the Discord bot code and command handling
- `pdf_processor.py`: Handles PDF text extraction and embedding creation
- `rag_system.py`: Implements the RAG system for generating responses

## 🤝 Contributing

Found a bug or have an idea for improvement? Contributions are welcome! Feel free to:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Built with [discord.py](https://discordpy.readthedocs.io/)
- Powered by [Google Gemini 2.0](https://ai.google/discover/gemini/)
- Vector storage by [ChromaDB](https://www.trychroma.com/)
- PDF processing with [PyPDF2](https://pypdf2.readthedocs.io/)

---

## 🔮 Future Enhancements

Some exciting features we're considering for future updates:

- Multi-PDF support for larger knowledge bases
- Image extraction and processing from PDFs
- User role-based access to different information
- Analytics dashboard for tracking common questions
- Custom personality settings for your bot

---

Made with ❤️ by Chun.
