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


## Architecture

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


# User Guide

## Overview

The AWS RAG Assistant allows users to ask natural language questions about the AWS Customer Agreement document. The system retrieves relevant document sections using semantic search and generates answers using an LLM.

---

## Starting the Application

### Step 1: Start the Backend

Open a terminal and run:

```bash
uvicorn main:app --reload
```

The FastAPI server will start at:

```
http://127.0.0.1:8000
```

Swagger API documentation is available at:

```
http://127.0.0.1:8000/docs
```

---

### Step 2: Start the Frontend

Open a second terminal and run:

```bash
streamlit run app.py
```

The Streamlit application will open automatically in your browser.

---

## Ingesting a Document

If the document has not been processed yet:

1. Open Swagger UI (`/docs`)
2. Use the `POST /ingest` endpoint
3. Provide the PDF path

Example:

```json
{
  "pdf_path": "data/AWS Customer Agreement.pdf"
}
```

The system will:

* Load the PDF
* Clean the text
* Split the document into chunks
* Generate embeddings
* Store vectors in ChromaDB

---

## Asking Questions

In the Streamlit interface:

1. Enter a question in the text box
2. Click the **Ask** button
3. View the generated answer
4. Expand the **Sources** section to view retrieved document chunks

Example questions:

* Can AWS terminate my account?
* What is AWS liability limit?
* Who owns customer content?
* What happens after termination?
* What are payment obligations?

---

## Analytics Dashboard

The Streamlit dashboard displays:

### Most Frequent Questions

Shows the questions asked most often.

### No Answer Queries

Shows questions for which the system could not find sufficient information.

### Average Latency

Displays the average response time for all queries.

---

## API Endpoints

### POST /ask

Submit a question to the RAG system.

Example:

```json
{
  "question": "Can AWS terminate my account?"
}
```

---

### POST /ingest

Processes a PDF and stores embeddings in ChromaDB.

Example:

```json
{
  "pdf_path": "data/AWS Customer Agreement.pdf"
}
```

---

### GET /analytics

Returns analytics information including:

* Most frequently asked questions
* Queries with no answer
* Average response latency

---

## Troubleshooting

### No Answer Returned

* Ensure the document has been ingested successfully.
* Verify that the question is related to the AWS Customer Agreement.

### Backend Not Running

Verify FastAPI is running:

```bash
uvicorn main:app --reload
```

### Frontend Not Loading

Verify Streamlit is running:

```bash
streamlit run app.py
```

### Missing API Key

Ensure the `.env` file contains a valid API key:

```env
GROQ_API_KEY=your_api_key
```

---

## Expected Workflow

1. Start FastAPI backend
2. Start Streamlit frontend
3. Ingest the AWS PDF (if required)
4. Ask questions
5. Review answers and sources
6. Monitor analytics dashboard

## Design Decisions

Chunk size 500 was selected to balance context preservation and retrieval precision. Smaller chunks may lose context while larger chunks can reduce retrieval accuracy.

Overlap helps preserve information that may span chunk boundaries.

Retrieving multiple chunks increases the likelihood that relevant context is available to the LLM.


## SnapShots 

<b> Ask Questions:</b>
<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/c10e8f39-ab16-4bd0-b099-7a2820d6f57d" />

<b>Sources:</b>
<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/27ee4c82-f282-4987-b4c4-7198cb127da2" />

<b>Most Asked Questions:</b>
<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/c85917f4-33a9-4bf8-be49-04da3cde8828" />

<b>No Answers Question:</b>
<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/5e4cf70d-26a8-466d-b04c-a970b13db7d5" />

<b>Latency:</b>
<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/45e26b84-241e-485a-bce0-900065967a98" />


<h3>Demo Question</h3>

Can AWS terminate my account?<br>
What is AWS liability limit?<br>
Who owns customer content?<br>
What happens after termination?<br>
What are payment obligations?<br>

<b>And invalid</b>

Who won IPL 2025?<br>
What is Python?
