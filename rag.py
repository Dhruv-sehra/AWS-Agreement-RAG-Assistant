from retriever import collection
from llm import generate_answer

def ask_question(question):

    results = collection.query(
        query_texts=[question],
        n_results=5
    )

    docs = results["documents"][0]

    context = "\n\n".join(docs)

    answer = generate_answer(
        question,
        context
    )

    return {
        "answer": answer,
        "sources": docs
    }