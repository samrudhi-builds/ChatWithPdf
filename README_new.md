# 📄 ChatWithPdf - AI-Powered PDF Question Answering

A **Streamlit web application** that allows users to upload PDF documents and ask questions about their content using **Retrieval Augmented Generation (RAG)** with local embeddings.

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-1.49+-red.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## 🌟 Features

- 📤 **PDF Upload**: Easy drag-and-drop PDF file upload
- 🧠 **Intelligent Q&A**: Ask natural language questions about your PDF content
- 🔍 **Semantic Search**: Uses sentence transformers for accurate content retrieval
- 💾 **Persistent Storage**: ChromaDB vector database maintains context between queries
- 🚀 **Local Processing**: No external APIs required - runs completely offline
- 🔄 **Multi-Query Support**: Ask multiple questions about the same document
- 🎯 **Session Management**: Smart handling of document processing and state

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **PDF Processing**: PyMuPDF (fitz)
- **Embeddings**: SentenceTransformers (`all-MiniLM-L6-v2`)
- **Vector Database**: ChromaDB
- **Language**: Python 3.8+

## 📋 Prerequisites

- Python 3.8 or higher
- pip package manager

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/Elysian0987/ChatWithPdf.git
cd ChatWithPdf
```

### 2. Navigate to Project Directory
```bash
cd askmypdf
```

### 3. Create Virtual Environment
```bash
python -m venv venv
```

### 4. Activate Virtual Environment

**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### 5. Install Dependencies
```bash
pip install streamlit sentence-transformers chromadb PyMuPDF
```

### 6. Run the Application
```bash
streamlit run app.py
```

### 7. Open in Browser
The app will automatically open at `http://localhost:8502`

## 📖 How to Use

1. **Upload PDF**: Click "Browse files" and select your PDF document
2. **Wait for Processing**: The app will extract text and create embeddings (one-time process)
3. **Ask Questions**: Type your questions in the text input field
4. **Get Answers**: View AI-generated responses based on your document content
5. **Ask More**: Continue asking questions - no need to re-upload the same PDF
6. **Reset**: Click "🔄 Reset" to upload a new PDF

### Example Questions
- "What is the main topic of this document?"
- "Summarize the key points in chapter 2"
- "What are the conclusions mentioned?"
- "List the important dates mentioned"

## 📁 Project Structure

```
ChatWithPdf/
├── askmypdf/
│   ├── app.py              # Main Streamlit application
│   ├── pdf_utils.py        # PDF text extraction utilities
│   ├── rag_utils.py        # RAG implementation and embeddings
│   ├── temp.pdf           # Temporary file for uploaded PDFs
│   ├── venv/              # Virtual environment
│   └── chroma_db/         # ChromaDB persistent storage
├── requirements.txt        # Python dependencies
├── packages.txt           # System packages (for deployment)
├── runtime.txt            # Python version specification
└── README.md              # This file
```

## 🔧 Configuration

### Chunking Parameters
In `rag_utils.py`, you can adjust text chunking:
```python
def split_text(text, chunk_size=500, overlap=50):
    # chunk_size: Characters per chunk
    # overlap: Characters to overlap between chunks
```

### Retrieval Parameters
Modify the number of chunks retrieved:
```python
results = collection.query(query_embeddings=[query_embedding], n_results=3)
# n_results: Number of relevant chunks to retrieve
```

## 🚀 Deployment

### Streamlit Cloud
1. Push your code to GitHub
2. Visit [share.streamlit.io](https://share.streamlit.io)
3. Connect your repository
4. Deploy!

### Local Network Access
```bash
streamlit run app.py --server.address 0.0.0.0
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🐛 Troubleshooting

### Common Issues

**"streamlit not recognized"**
- Make sure your virtual environment is activated
- Reinstall streamlit: `pip install streamlit`

**"Import chromadb could not be resolved"**
- Install chromadb: `pip install chromadb`
- Ensure virtual environment is activated

**App runs but accuracy is poor**
- Current implementation uses a simple local response system
- For better accuracy, consider integrating OpenAI GPT or local LLM

**PDF processing fails**
- Ensure PDF is not password-protected
- Check if PDF contains extractable text (not just images)

### Performance Notes
- First query after upload takes longer (embedding creation)
- Subsequent queries are faster (using cached embeddings)
- Large PDFs may take more time to process

## 🔮 Future Enhancements

- [ ] OpenAI GPT integration for better responses
- [ ] Support for multiple file formats (DOCX, TXT)
- [ ] Conversation history
- [ ] Advanced chunking strategies
- [ ] Custom embedding models
- [ ] Multi-language support
- [ ] Export conversation as PDF/TXT

## 👨‍💻 Author

**Elysian0987**
- GitHub: [@Elysian0987](https://github.com/Elysian0987)

## 🙏 Acknowledgments

- [Streamlit](https://streamlit.io/) for the amazing web framework
- [ChromaDB](https://www.trychroma.com/) for vector database
- [SentenceTransformers](https://www.sbert.net/) for embeddings
- [PyMuPDF](https://pymupdf.readthedocs.io/) for PDF processing

---

⭐ **If you found this project helpful, please give it a star!** ⭐
