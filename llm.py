from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
client = OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1"
)

def generate_answer(question, context):

    prompt = f"""
    You are a document QA assistant.

    Answer ONLY using the provided context.

    If the answer is not contained in the context,
    reply exactly:

    Answer not found in document.

    CONTEXT:
    {context}

    QUESTION:
    {question}
    """
    
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )
    return response.choices[0].message.content