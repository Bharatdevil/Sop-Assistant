from app.pinecone_store import search_query
from app.llm import generate_answer


print("HR Policy Assistant")
print("Type 'exit' to stop.\n")

while True:
    query = input("Ask question: ")

    if query.lower() == "exit":
        print("Goodbye!")
        break
        
    results = search_query(query)

    answer = generate_answer(results,query)

    print("\nAnswer:")
    print(answer)
    print("-" * 50)