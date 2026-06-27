# 📄 AI Document Q&A Bot (RAG Pipeline)

An AI-powered Document Question Answering application built using **Python**, **LangChain**, **Google Gemini**, **ChromaDB**, and **Streamlit**.

The application allows users to upload documents, build a vector database, and ask natural language questions about the uploaded documents.

---

## 🚀 Features

* 📄 PDF Document Loading
* 📚 Document Chunking
* 🧠 HuggingFace Embeddings
* 🗂️ Chroma Vector Database
* 🔎 Semantic Search
* 🤖 Google Gemini 2.5 Flash
* 💬 Chat Interface using Streamlit
* 📌 Source Document Display
* 📤 Upload New PDF
* 🗑️ Clear Chat

---

## 🛠️ Tech Stack

* Python 3.12
* LangChain
* Google Gemini API
* ChromaDB
* HuggingFace Embeddings
* Streamlit
* Sentence Transformers

---

## 📁 Project Structure

```
document-qa-bot/
│
├── app.py
├── index_documents.py
├── requirements.txt
├── README.md
├── .env
├── docs/
├── chroma_db/
│
└── src/
    ├── loader.py
    ├── chunker.py
    ├── vector_store.py
    ├── retriever.py
    ├── llm.py
    ├── rag_chain.py
    └── indexer.py
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone <your-github-repository-url>
cd document-qa-bot
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it (Windows):

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```text
GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY
```

---

## ▶️ Run the Project

Index the documents:

```bash
python index_documents.py
```

Run the application:

```bash
streamlit run app.py
```

---

## 📸 Screenshots

Add screenshots of:

* Home Page
* Asking Questions
* Source Documents
* Upload PDF

---

## 📈 Future Improvements

* Multi-PDF Support
* Conversation Memory
* Streaming Responses
* Deployment on Streamlit Cloud
* Better UI
* Hybrid Search

---

## 👨‍💻 Author

Created as an AI Internship Technical Assignment.

Built using Python, LangChain, ChromaDB, Google Gemini, and Streamlit.
