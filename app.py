import os
import streamlit as st

from src.rag_chain import create_rag_chain
from src.indexer import index_documents

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Document Q&A Bot",
    page_icon="📄",
    layout="wide"
)

# --------------------------------------------------
# Load RAG Chain
# --------------------------------------------------

@st.cache_resource
def load_chain():
    return create_rag_chain()


rag_chain = load_chain()

# --------------------------------------------------
# Session State
# --------------------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

# --------------------------------------------------
# Sidebar
# --------------------------------------------------

with st.sidebar:

    st.title("📄 Document Q&A Bot")

    st.markdown("---")

    st.write("### About")
    st.write("""
Ask questions about the documents stored in the **docs** folder.

Supported formats:

- PDF
- DOCX
- TXT
""")

    st.markdown("---")

    st.subheader("📤 Upload PDF")

    uploaded_file = st.file_uploader(
        "Choose a PDF",
        type=["pdf"]
    )

    if uploaded_file is not None:

        os.makedirs("docs", exist_ok=True)

        save_path = os.path.join("docs", uploaded_file.name)

        if not os.path.exists(save_path):

            # Save uploaded file
            with open(save_path, "wb") as f:
                f.write(uploaded_file.getbuffer())

            # Index all documents
            with st.spinner("Indexing document..."):
                index_documents()

            st.success("✅ Document indexed successfully!")

            # Reload RAG
            st.cache_resource.clear()

            st.rerun()

        else:
            st.warning("⚠️ This document already exists.")

    st.markdown("---")

    if st.button("🗑️ Clear Chat"):

        st.session_state.messages = []

        st.rerun()

# --------------------------------------------------
# Main Page
# --------------------------------------------------

st.title("🤖 AI Document Assistant")

st.caption("Powered by LangChain • ChromaDB • Gemini")

# --------------------------------------------------
# Display Previous Messages
# --------------------------------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --------------------------------------------------
# Chat Input
# --------------------------------------------------

question = st.chat_input("Ask a question about your documents...")

if question:

    # User message

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    # Assistant response

    with st.chat_message("assistant"):

        with st.spinner("Searching documents..."):

            response = rag_chain.invoke(
                {
                    "input": question
                }
            )

        answer = response["answer"]

        st.markdown(answer)

        # Show Sources

        if "context" in response:

            with st.expander("📚 Sources Used"):

                shown = set()

                for doc in response["context"]:

                    source = doc.metadata.get("source", "Unknown")
                    page = doc.metadata.get("page", "Unknown")

                    key = (source, page)

                    if key not in shown:

                        shown.add(key)

                        st.write(f"📄 {source} | Page {page}")

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )