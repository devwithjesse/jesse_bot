import os
from langchain_chroma import Chroma
from src.config import CHROMA_PERSIST_DIR
from src.rag.embeddings.gemini import GeminiEmbedding
from src.rag.embeddings.hf import HFEmbedding

_vectorstore_instance = None

def get_embedding_provider(name="hf"):
    return HFEmbedding() if name == "hf" else GeminiEmbedding()

def get_vectorstore(provider_name="hf") -> Chroma:
    global _vectorstore_instance

    if _vectorstore_instance is None:
        if not os.path.exists(CHROMA_PERSIST_DIR):
            os.makedirs(CHROMA_PERSIST_DIR)

        # Initialize ONLY if it doesn't exist yet
        _vectorstore_instance = Chroma(
            collection_name="knowledge_base",
            embedding_function=get_embedding_provider(provider_name),
            persist_directory=str(CHROMA_PERSIST_DIR/"hf") if provider_name=="hf" else str(CHROMA_PERSIST_DIR/"gemini"),
        )
    
    return _vectorstore_instance

def embed_text(chunks, ids, metadatas=None):
    vectorstore = get_vectorstore()
    
    if metadatas is None:
        metadatas = [{} for _ in range(len(chunks))]

    # Gemini batch limit is 100
    batch_size = 100 
    
    for i in range(0, len(chunks), batch_size):
        
        batch_chunks = chunks[i : i + batch_size]
        batch_ids = ids[i : i + batch_size]
        batch_metadatas = metadatas[i : i + batch_size]
        
        print(f"Ingesting batch {i//batch_size + 1} ({len(batch_chunks)} chunks)...")
        
        vectorstore.add_texts(
            texts=batch_chunks,
            metadatas=batch_metadatas,
            ids=batch_ids
        )

    print(f"Successfully ingested all {len(chunks)} chunks.")