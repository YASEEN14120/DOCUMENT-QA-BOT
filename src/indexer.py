from src.loader import load_documents
from src.chunker import split_documents
from src.vector_store import create_vector_store


def index_documents():

    print("Loading documents...")

    documents = load_documents()

    print(f"{len(documents)} pages loaded.")

    chunks = split_documents(documents)

    print(f"{len(chunks)} chunks created.")

    create_vector_store(chunks)

    print("Indexing complete.")

    return len(documents), len(chunks)