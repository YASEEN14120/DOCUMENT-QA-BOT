from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_classic.chains import create_retrieval_chain
from langchain_core.prompts import ChatPromptTemplate

from src.llm import load_llm
from src.retriever import get_retriever


def create_rag_chain():

    llm = load_llm()

    retriever = get_retriever()

    prompt = ChatPromptTemplate.from_template(
        """
You are an intelligent AI assistant.

Answer ONLY using the provided context.

If the answer cannot be found in the context, reply:

"I don't know based on the uploaded documents."

Keep answers clear and concise.

<context>
{context}
</context>

Question:
{input}

Answer:
"""
    )

    document_chain = create_stuff_documents_chain(
        llm,
        prompt,
    )

    retrieval_chain = create_retrieval_chain(
        retriever,
        document_chain,
    )

    return retrieval_chain