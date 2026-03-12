import warnings
warnings.filterwarnings("ignore")
from fastapi import FastAPI,Request
from pydantic import BaseModel

from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.middleware import SlowAPIMiddleware
from slowapi.errors import RateLimitExceeded
from slowapi import _rate_limit_exceeded_handler


from query import ask_question

app = FastAPI()

limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
app.add_middleware(SlowAPIMiddleware)

class Question(BaseModel):
    question: str



@app.get("/")
def home():
    return {"message": " RAG API Running"}

@app.post("/ask")
@limiter.limit("2/minute")
def ask(request: Request,data: Question):

    answer ,sources = ask_question(data.question)
    
    return {
        "answer": answer,
        "sources":sources}

