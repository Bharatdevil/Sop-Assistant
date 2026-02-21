from app.ingestion import load_documents
from app.chunking import split_documents
from app.embeddings import get_embeddings
from app.vectorstore import create_vector_store

# Step 1: Load
docs = load_documents()

# Step 2: Split
chunks = split_documents(docs)

# Step 3: Embeddings
embeddings = get_embeddings()

# Step 4: Create FAISS vector store
vectorstore = create_vector_store(chunks, embeddings)

print("Total pages:", len(docs))
print("Total chunks:", len(chunks))
print("chunks 1:", chunks[0])
print("chunks 2:", chunks[1])

print("Total vectors stored in FAISS:", vectorstore.index.ntotal)
print("Vector store created successfully!")


print("\n--- Similarity Search Test ---")
results = vectorstore.similarity_search("How many days of paid annual leave are employees entitled to ?", k=2)

for i, doc in enumerate(results):
    print(f"\nResult {i+1}:")
    print(doc.page_content[:300])