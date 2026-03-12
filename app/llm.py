from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

def generate_answer(context, question):
    """This is chat with query function"""
    gemini_api_key = os.getenv("GEMINI_API_KEY")
    client = genai.Client(api_key=gemini_api_key)

    system_prompt = f"""
    You are an intelligent document assistant.

    Your task is to answer the user's question using ONLY the information from the provided context.

    Instructions:
    - Provide a clear and detailed explanation.
    - Expand the answer so it is easy to understand.
    - Use multiple sentences if needed.
    - Do not make up information outside the context.
    - If the answer is not present in the context, respond:
    "This question is outside the provided documents.
    Context:{context}
    Question:{question}
    """

    response = client.models.generate_content(
        model="gemini-3.1-flash-lite-preview",
        contents=system_prompt
    )
    return response.text

