from langchain_openai import ChatOpenAI

from prompts.extraction_prompt import EXTRACTION_PROMPT


class ExtractionAgent:

    def run(self, text):

        llm = ChatOpenAI()

        response = llm.invoke(
            EXTRACTION_PROMPT + text
        )

        return response.content