from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

def generate_answer(context, question):
    """This is chat with query function"""
    
    gemini_api_key = os.getenv("GEMINI_API_KEY")
    client = genai.Client(api_key=gemini_api_key)

    system_prompt = f"""
    You are an HR assistant.

    Use ONLY the information provided in the context below.

    Important rules:
    1. Do NOT add information that is not in the context.
    2. Ignore unrelated sections of the context.
    3. If the context does not contain the answer, respond exactly:
    "This question is outside the provided documents."

    Answer clearly and naturally.

    Context:{context}
    Question:{question}
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=system_prompt
    )
    return response.text

