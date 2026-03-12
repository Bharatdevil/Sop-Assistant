from app.pinecone_store import search_query
from app.genai import generate_answer


def ask_question(question):
    contexts, sources = search_query(question)

    context_text = "\n".join(contexts)

    answer = generate_answer(context_text, question)
    if "outside the provided documents" in answer.lower():
        sources = []

    return answer, sources
