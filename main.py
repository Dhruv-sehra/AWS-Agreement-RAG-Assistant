from fastapi import FastAPI
from pydantic import BaseModel
from analytics import get_analytics
import time
from rag import ask_question
from ingest import ingest_document
app = FastAPI()

class QuestionRequest(BaseModel):
    question: str

class IngestRequest(BaseModel):
    pdf_path: str

@app.get("/")
def home():
    return {"status running"}


@app.post("/ask")
def ask(request: QuestionRequest):
    from database import SessionLocal
    from models import QueryLog
    if not request.question.strip():
        return {
            "error":"Question cannot be empty"
        }

    start = time.time()

    result = ask_question(
        request.question
    )
    latency = time.time() - start

    db = SessionLocal()

    log = QueryLog(
        question=request.question,
        answer=result["answer"],
        answer_found=(
            0 if "Answer not found"
            in result["answer"]
            else 1
        ),
        latency=latency
    )

    db.add(log)
    db.commit()

    db.close()

    result["latency"] = latency
    return result

@app.get("/analytics")
def analyse():
    return get_analytics()

@app.post("/ingest")
def ingest(request: IngestRequest):

    return ingest_document(
        request.pdf_path
    )