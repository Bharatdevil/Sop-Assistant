from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

def get_embeddings(text):
    api_key = os.getenv("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    response = client.models.embed_content(
        model="gemini-embedding-001",
        contents=text
    )

    return response.embeddings[0].values
