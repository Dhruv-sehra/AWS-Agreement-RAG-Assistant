from pdfloader import load_pdf
from chunker import chunk_text
from embedding import get_embeddings
import chromadb

def ingest_document(pdf_path):

    text = load_pdf(pdf_path)

    chunks = chunk_text(text)

    vectors = get_embeddings(chunks)

    client = chromadb.PersistentClient(
        path="chroma_db"
    )

    try:
        client.delete_collection("aws_docs")
    except:
        pass

    collection = client.get_or_create_collection(
        "aws_docs"
    )

    collection.add(
        ids=[str(i) for i in range(len(chunks))],
        documents=chunks,
        embeddings=vectors
    )

    return {
        "message": "Document ingested",
        "chunks": len(chunks)
    }