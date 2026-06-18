<h1>AWS Agreement RAG Assistant</h1>

A Retrieval-Augmented Generation (RAG) system that allows users to ask questions about the AWS Customer Agreement document.

The system retrieves relevant document chunks using semantic search and generates answers using an LLM.


                                                            AWS Agreement PDF
                                                                   ↓
                                                                 PyPDF
                                                                   ↓
                                                                Chunking
                                                                   ↓
                                                      SentenceTransformer (Embeddings)
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


<h3>Design Decisions</h3>

Chunk size 500 was selected to balance context preservation and retrieval precision. Smaller chunks may lose context while larger chunks can reduce retrieval accuracy.

Overlap helps preserve information that may span chunk boundaries.

Retrieving multiple chunks increases the likelihood that relevant context is available to the LLM.

<h3>API Endpoints</h3>

POST /ask
GET /analytics
POST /ingest

<h2>Architecture</h2>

rag_assignment/<br>
│
├── main.py<br>
├── app.py<br>
├── rag.py<br>
├── retriever.py<br>
├── llm.py<br>
├── pdfloader.py<br>
├── chunker.py<br>
├── embedding.py<br>
├── analytics.py<br>
├── database.py<br>
├── models.py<br>
│<br>
├── data/<br>
├── chroma_db/<br>
├── logs.db<br>
│<br>
├── requirements.txt<br>
└── README.md<br>



<h3>Demo Question</h3>

Can AWS terminate my account?<br>
What is AWS liability limit?<br>
Who owns customer content?<br>
What happens after termination?<br>
What are payment obligations?<br>

<b>And invalid</b>

Who won IPL 2025?<br>
What is Python?
