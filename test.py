from rag import ask_question

question = input("Question: ")

response = ask_question(question)

print("\nANSWER:\n")
print(response["answer"])

print("\nSOURCES:\n")

for source in response["sources"]:
    print(source[:300])
    print("-" * 50)