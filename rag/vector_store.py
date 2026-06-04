from langchain_community.vectorstores import Chroma
from rag.embeddings import embeddings

vectordb = Chroma(
    persist_directory="chroma_db",
    embedding_function=embeddings
)