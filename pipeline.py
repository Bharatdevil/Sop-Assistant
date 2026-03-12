from app.ingestion import load_documents
from app.chunking import split_documents
from app.pinecone_store import create_pinecone_index

# Step 1: Load
docs = load_documents()

# Step 2: Split
chunks = split_documents(docs)

# to check chunks
# print(chunks)
# print("chunks 1:", chunks[0])
# print("chunks 2:", chunks[1])

# Step 4: Create FAISS vector store
create_pinecone_index(chunks)
print("Ingestion complete ✅")
# print("Total pages:", len(docs))
# print("Total chunks:", len(chunks))
# print("chunks 1:", chunks[0])
# print("chunks 2:", chunks[1])