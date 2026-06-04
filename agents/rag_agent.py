from langchain_openai import ChatOpenAI

from rag.retriever import retrieve


class RAGAgent:

    def run(self, question):

        docs = retrieve(question)

        context = "\n".join(
            [d.page_content for d in docs]
        )

        llm = ChatOpenAI()

        prompt = f"""
        Context:
        {context}

        Question:
        {question}
        """

        return llm.invoke(prompt).content