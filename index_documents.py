from dotenv import load_dotenv

from src.loader import load_documents
from src.chunker import split_documents
from src.vector_store import create_vector_store

load_dotenv()

print("Loading documents...")
documents = load_documents()

print(f"Loaded {len(documents)} pages.")

print("Splitting documents...")
chunks = split_documents(documents)

print(f"Created {len(chunks)} chunks.")

print("Creating vector database...")
create_vector_store(chunks)

print("✅ Indexing completed successfully!")