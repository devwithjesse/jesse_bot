from langchain_core.callbacks import BaseCallbackHandler
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
from src.rag.retriever import retrieve_documents
from src.config import GEMINI_API_KEY, GROQ_API_KEY, LLM_MODEL
from src.utils.logger import setup_logger
from pathlib import Path

logger = setup_logger("llm")

class FallBackLoggingHandler(BaseCallbackHandler):
    def on_llm_error(self, error, **kwargs):
        # This triggers the moment the primary LLM (Gemini) fails
        logger.warning(f"Primary LLM failed with error: {error}. Falling back to secondary LLM.")

# 1. Define Primary (Gemini)
gemini_llm = ChatGoogleGenerativeAI(
        model=LLM_MODEL,
        api_key=GEMINI_API_KEY,
        max_retries=1
    )

# 2. Define fallback (Groq)
groq_llm = ChatGroq(
    model_name="llama-3.3-70b-versatile",
    groq_api_key=GROQ_API_KEY
)

def generate(prompt):

    llm_with_fallback = gemini_llm.with_fallbacks([groq_llm]).with_config(
        callbacks=[FallBackLoggingHandler()]
    )

    return llm_with_fallback.invoke(prompt).content

def build_prompt(query, source):
    """
    Builds a structured RAG prompt with context and user query
    """

    prompt_path = Path(__file__).parent.parent.parent / "rag_prompt.txt"

    context = "\n\n".join([doc.page_content for doc in source])

    with open(prompt_path, encoding="utf-8") as reader:
        prompt = reader.read()

    return prompt.format(context=context, query=query)


def query_llm(question):
    results = retrieve_documents(question)
    rag_prompt = build_prompt(question, results)
    response = generate(rag_prompt)

    return response

