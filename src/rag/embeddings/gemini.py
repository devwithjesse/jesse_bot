from google import genai
from google.genai import types
from typing import List
from langchain_core.embeddings import Embeddings
from src.config import GEMINI_EMBEDDING_MODEL, GEMINI_API_KEY

class GeminiEmbedding(Embeddings):

    def __init__(self):
        self.client = genai.Client(api_key=GEMINI_API_KEY)
        self.dimension = 768

    def embed_query(self, text: str) -> List[float]:
        return self.embed_documents([text])[0]

    def embed_documents(self, texts: List[str]):
        result = self.client.models.embed_content(
            model=GEMINI_EMBEDDING_MODEL,
            contents=texts,
            config=types.EmbedContentConfig(output_dimensionality=self.dimension)   
        )

        return [embedding.values for embedding in result.embeddings]