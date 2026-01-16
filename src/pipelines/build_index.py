import hashlib
from src.rag.loader import load_data
from src.rag.splitter import get_chunks
from src.rag.vectorstore import embed_text
from src.config import KB_PATH

def generate_chunk_id(text):
    """Generates a unique ID for a text chunk using SHA256 hash."""
    return hashlib.sha256(text.encode('utf-8')).hexdigest()

def build_index():
    print("Loading knowledge base...")

    raw = load_data(KB_PATH)
    documents = get_chunks(raw)

    chunks = []
    metadatas = []
    ids = []

    for doc in documents:

        chunk_id = generate_chunk_id(doc.page_content)

        chunks.append(doc.page_content)
        ids.append(chunk_id)

        # Merge existing header metadata with source info
        meta = doc.metadata.copy()
        meta["source"] = str(KB_PATH)
        metadatas.append(meta)

    print(f"Total chunks to sync: {len(chunks)}")


    # ingest database
    embed_text(chunks=chunks, ids=ids, metadatas=metadatas)

    print("Database sync complete")
