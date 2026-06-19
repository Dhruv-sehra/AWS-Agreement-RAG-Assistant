import chromadb

def retrieve(question, top_k=5):

    client = chromadb.PersistentClient(
        path="chroma_db"
    )

    collection = client.get_collection(
        "aws_docs"
    )

    results = collection.query(
        query_texts=[question],
        n_results=top_k
    )

    return results["documents"][0]
