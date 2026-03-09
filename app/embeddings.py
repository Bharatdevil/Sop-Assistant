# import os
import os
# Disable HuggingFace warnings
os.environ["HF_HUB_DISABLE_TELEMETRY"] = "1"
os.environ["HF_HUB_DISABLE_PROGRESS_BARS"] = "1"
os.environ["TRANSFORMERS_VERBOSITY"] = "error"

from transformers import logging
logging.set_verbosity_error()

from dotenv import load_dotenv
from huggingface_hub import login

load_dotenv()   # this loads .env file

login(os.getenv("HF_TOKEN"))

from sentence_transformers import SentenceTransformer

# Load embedding model once
model = SentenceTransformer("all-MiniLM-L6-v2")

def get_embeddings(text):
    embedding = model.encode(text)
    return embedding.tolist()