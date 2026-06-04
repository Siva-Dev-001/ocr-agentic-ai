from langchain_openai import ChatOpenAI


class SummaryAgent:

    def run(self, text):

        llm = ChatOpenAI()

        return llm.invoke(
            f"Summarize:\n{text}"
        ).content