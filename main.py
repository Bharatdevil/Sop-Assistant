from fastapi import FastAPI
from pydantic import BaseModel

from app.pinecone_store import search_query
from app.llm import generate_answer

app = FastAPI(title="HR Policy RAG Assistant")

class Question(BaseModel):
    question: str

@app.post("/ask")
def ask_question(data: Question):

    query = data.question

    context = search_query(query)

    answer = generate_answer(context, query)

    return {
        "question": query,
        "answer": answer
    }