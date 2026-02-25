# AI Multi-Document Chatbot with Memory (RAG)

A production-ready conversational assistant that allows users to upload multiple PDF documents and ask natural language questions. It uses semantic search (RAG) and Google Gemini API for context-aware answers.

## 🚀 Features

- **Document Upload**: Upload multiple PDFs simultaneously.
- **RAG Architecture**: Uses LangChain, FAISS, and Sentence Transformers for efficient document retrieval.
- **Google Gemini LLM**: Leverages `gemini-1.5-flash` for high-quality responses.
- **Conversational Memory**: Remembers past interactions for context-aware chatting.
- **Source Citation**: Displays the exact chunks/documents used to generate the answer.
- **Streamlit UI**: A sleek, dark-themed, and responsive web interface.

## 🏗 Architecture

1. **Frontend**: Streamlit UI for user interaction.
2. **Document Loader**: Extracts text from PDFs using `PyPDFLoader`.
3. **Text Splitter**: Chunks text for better semantic granularity.
4. **Embeddings**: `all-MiniLM-L6-v2` from Sentence Transformers.
5. **Vector Store**: FAISS for fast local similarity search.
6. **LLM**: Google Gemini (`gemini-1.5-flash`).
7. **Memory**: LangChain `ConversationBufferMemory`.

## 🛠 Installation

### 1. Prerequisites
- Python 3.10+
- Google Cloud Project with Gemini API access.

### 2. Clone the Repository
```bash
git clone <repository-url>
cd ai-multi-doc-chatbot
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Setup Environment Variables
Create a `.env` file in the root directory and add your Google API key:
```env
GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY
```

## 🚀 Running the App

```bash
streamlit run app.py
```

## 🔑 How to create Google API Key
1. Go to [Google AI Studio](https://aistudio.google.com/).
2. Sign in with your Google account.
3. Click on **"Get API key"** in the sidebar.
4. Create a new API key.

## 📄 License
MIT License
