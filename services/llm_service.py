from langchain_openai import ChatOpenAI


class LLMService:

    def __init__(self):

        self.llm = ChatOpenAI(
            temperature=0
        )

    def generate(self, prompt):

        response = self.llm.invoke(prompt)

        return response.content