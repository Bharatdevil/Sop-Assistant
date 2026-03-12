import os

os.environ["HF_HUB_DISABLE_TELEMETRY"] = "1"
os.environ["HF_HUB_DISABLE_PROGRESS_BARS"] = "1"
os.environ["TRANSFORMERS_VERBOSITY"] = "error"

from transformers import logging
logging.set_verbosity_error()


from sentence_transformers import SentenceTransformer

#embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

def get_embeddings(text):
    embedding = model.encode(text)
    return embedding.tolist()