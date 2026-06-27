from src.rag_chain import create_rag_chain

rag = create_rag_chain()

response = rag.invoke(
    {
        "input": "What is Artificial Intelligence?"
    }
)

print("\nAnswer:\n")
print(response["answer"])