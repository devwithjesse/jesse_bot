from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

TELEGRAM_BOT_API_TOKEN = os.getenv("TELEGRAM_BOT_API_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
CHROMA_PERSIST_DIR = BASE_DIR / (os.getenv("CHROMA_PERSIST_DIR", "chroma/db"))
KB_PATH = os.getenv("KB_PATH", str(BASE_DIR / "data/knowledge_base.md"))
HF_EMBEDDING_MODEL = os.getenv("HF_EMBEDDING_MODEL", "sentence-transformers/all-MiniLM-L6-v2")
GEMINI_EMBEDDING_MODEL = os.getenv("GEMINI_EMBEDDING_MODEL", "text-embedding-004")
LLM_MODEL = os.getenv("LLM_MODEL", "gemini-3-pro")
TOP_K = int(os.getenv("TOP_K", 3))
PORT = int(os.getenv("PORT", 5000))
HF_TOKEN = os.getenv("HF_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
NGROK_TEST_URL = os.getenv("NGROK_TEST_URL")

