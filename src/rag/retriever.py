from src.rag.vectorstore import get_vectorstore
from src.config import TOP_K

def retrieve_documents(query_text: str, k=None):
    """
    Retrieves the top-k similar documents (chunks) from Chroma.
    """
    
    if k is None:
        k = TOP_K

    try:
        # 1. Gemini
        vectorstore = get_vectorstore(provider_name="gemini")
        return vectorstore.as_retriever(search_kwargs={"k":k}).invoke(query_text)

    except Exception as e:
        if "429" in str(e):
            # Quota reached
            #2. Fallback to minilm
            vectorstore = get_vectorstore(provider_name="gemini")
            return vectorstore.as_retriever(search_kwargs={"k":k}).invoke(query_text)
