from langchain_huggingface import HuggingFaceEndpointEmbeddings
from src.config import HF_TOKEN, HF_EMBEDDING_MODEL

class HFEmbedding:
    def __init__(self):
        self.model = HuggingFaceEndpointEmbeddings(
            model=HF_EMBEDDING_MODEL,
            huggingfacehub_api_token=HF_TOKEN
        )

    def embed_documents(self, texts):
        return self.model.embed_documents(texts)
    
    def embed_query(self, text):
        return self.model.embed_query(text)