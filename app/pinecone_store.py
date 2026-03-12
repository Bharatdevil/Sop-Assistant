from pinecone import Pinecone
import os
from dotenv import load_dotenv
from app.embeddings import get_embeddings

load_dotenv()

api_key = os.getenv("PINECONE_API_KEY")
host = os.getenv("HOST")

pc = Pinecone(api_key=api_key)
index = pc.Index(host=host)


def create_pinecone_index(chunks):

    vectors = []

    for i, chunk in enumerate(chunks):

        embedding = get_embeddings(chunk.page_content)

        vectors.append({
            "id": f"chunk_{i}",
            "values": embedding,
            "metadata": {
                "text": chunk.page_content,
                "page": chunk.metadata.get("page"),
                "source": chunk.metadata.get("source")
            }
        })

    # Upload vectors to Pinecone
    index.upsert(vectors=vectors)

    print(f"Uploaded {len(vectors)} vectors to Pinecone")


def search_query(query:str):
    # 1 Convert query to vector
    query_embedding = get_embeddings(query)

    results=index.query(
        vector=query_embedding,
        top_k=5,
        include_metadata=True
    )
    contexts = []
    sources=[]
    seen = set()

    for match in results["matches"]:
        metadata = match["metadata"]

        contexts.append(metadata["text"])
        source_tuple = (metadata.get("source"), metadata.get("page"))
        if source_tuple not in seen:
            sources.append({
                "document": metadata.get("source"),
                "page": metadata.get("page")
            })
            seen.add(source_tuple)

    return contexts, sources