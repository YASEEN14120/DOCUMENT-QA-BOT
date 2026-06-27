from src.loader import load_documents
from src.chunker import split_documents

documents = load_documents()

print(f"Loaded {len(documents)} pages.")

chunks = split_documents(documents)

print(f"Created {len(chunks)} chunks.")

print("\nFirst chunk:\n")
print(chunks[0].page_content[:500])