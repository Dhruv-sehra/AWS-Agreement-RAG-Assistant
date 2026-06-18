import chromadb
# from chunker import chunks
# from embedding import vectors
client = chromadb.PersistentClient(
    path="chroma_db"
)

collection = client.get_or_create_collection(
    "aws_docs"
)

# collection.add(
#     ids=[str(i) for i in range(len(vectors))],
#     documents=chunks,
#     embeddings=vectors
# )

# print(collection.peek())

# results = collection.query(
#     query_texts=[
#         "Can AWS terminate my account?"
#     ],
#     n_results=3
# )

# print(
#     results["documents"][0]
# )

