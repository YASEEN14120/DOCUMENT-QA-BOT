from src.retriever import get_retriever

retriever = get_retriever()

query = "What is Artificial Intelligence?"

results = retriever.invoke(query)

print(f"Retrieved {len(results)} documents\n")

for i, doc in enumerate(results, 1):
    print("=" * 60)
    print(f"Result {i}")
    print(doc.page_content[:500])