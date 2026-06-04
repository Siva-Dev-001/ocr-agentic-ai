from langchain_openai import OpenAIEmbeddings


class EmbeddingService:

    def __init__(self):
        self.embedding_model = OpenAIEmbeddings()

    def generate_embedding(self, text):

        return self.embedding_model.embed_query(text)