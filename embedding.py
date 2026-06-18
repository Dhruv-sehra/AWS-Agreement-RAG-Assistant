from sentence_transformers import SentenceTransformer
# from chunker import chunks

# text = load_pdf("data/AWS Customer Agreement.pdf")

print("⏳ Initializing SentenceTransformer model...")

model = SentenceTransformer("all-MiniLM-L6-v2")


def get_embeddings(chunks):

    return model.encode(
        chunks
    ).tolist()

# print(embeddings.shape)

# vectors = get_embeddings(
#     chunks
# )

# print(len(vectors))
# print(len(vectors[0]))
