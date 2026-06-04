from rag.vector_store import vectordb

def retrieve(query):

    docs = vectordb.similarity_search(
        query,
        k=5
    )

    return docs