AWS Agreement RAG Assistant

A Retrieval-Augmented Generation (RAG) system that allows users to ask questions about the AWS Customer Agreement document.

The system retrieves relevant document chunks using semantic search and generates answers using an LLM.


   PDF
    ↓
  PyPDF
    ↓
 Chunking
    ↓
SentenceTransformer
    ↓
ChromaDB
    ↓
Retriever
    ↓
LLM (Groq/Grok)
    ↓
Answer
    ↓
SQLite
    ↓
Analytics



Frontend:
- Streamlit

Backend:
- FastAPI

Vector Database:
- ChromaDB

Embedding Model:
- all-MiniLM-L6-v2

LLM:
- Groq (Llama 3.3)

Database:
- SQLite


Design Decisions

Chunk size 500 was selected to balance context preservation and retrieval precision. Smaller chunks may lose context while larger chunks can reduce retrieval accuracy.

Overlap helps preserve information that may span chunk boundaries.

Retrieving multiple chunks increases the likelihood that relevant context is available to the LLM.

API Endpoints

POST /ask
GET /analytics
POST /ingest


rag_assignment/
│
├── main.py
├── app.py
├── rag.py
├── retriever.py
├── llm.py
├── pdfloader.py
├── chunker.py
├── embedding.py
├── analytics.py
├── database.py
├── models.py
│
├── data/
├── chroma_db/
├── logs.db
│
├── requirements.txt
└── README.md



Demo Question

Can AWS terminate my account?
What is AWS liability limit?
Who owns customer content?
What happens after termination?
What are payment obligations?

And invalid

Who won IPL 2025?
What is Python?