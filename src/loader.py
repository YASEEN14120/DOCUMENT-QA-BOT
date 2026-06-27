from pathlib import Path

from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
    Docx2txtLoader,
)


def load_documents(docs_folder="docs"):
    """
    Load PDF, DOCX and TXT files from the docs folder.
    """

    documents = []

    docs_path = Path(docs_folder)

    for file in docs_path.iterdir():

        if file.suffix.lower() == ".pdf":
            loader = PyPDFLoader(str(file))
            documents.extend(loader.load())

        elif file.suffix.lower() == ".docx":
            loader = Docx2txtLoader(str(file))
            documents.extend(loader.load())

        elif file.suffix.lower() == ".txt":
            loader = TextLoader(str(file), encoding="utf-8")
            documents.extend(loader.load())

    return documents