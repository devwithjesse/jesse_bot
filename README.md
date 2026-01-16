# 🤖 JesseBot: Personal RAG-Powered Telegram Assistant

**JesseBot** is a high-performance Retrieval-Augmented Generation (RAG) chatbot designed to represent the identity, skills, and background of **Jesse Mokolo**. Built with a modular Python architecture, it uses semantic search to provide grounded, accurate answers about Jesse's life and career.

---

## 🚀 Key Features
- **RAG Architecture:** Uses LangChain and ChromaDB to retrieve facts from a custom Markdown knowledge base.
- **Dual-Model Fallback:** Primary processing via **Gemini 1.5 Flash**, with automatic fallback to **Groq (Llama 3.3 70B)** to ensure 100% uptime.
- **Hybrid Embeddings:** Powered by **Hugging Face Inference API** (Cloud) for zero-latency indexing without the local bloat.
- **Dynamic Handlers:** Support for `/chat`, `/image` (personal gallery), and `/info` commands.
- **Cloud-Ready:** Optimized for **Render** and **Google Cloud Run** using a Flask-based Webhook architecture.

---

## 🛠 Tech Stack
- **Language:** Python 3.11+
- **Orchestration:** LangChain
- **Vector Database:** ChromaDB
- **Models:** Google Gemini 1.5 Flash & Groq (Llama 3.3 70B)
- **Web Framework:** Flask (Webhook)
- **Embedding Provider:** Hugging Face Hub (Inference API)

---

## 📁 Project Structure
```text
JesseBot/
├── assets/             # Personal images for /image command
├── src/
│   ├── pipelines/      # RAG build_index logic
│   ├── rag/            # LLM, Vectorstore, and Splitter configurations
│   ├── telegram/       # Bot handlers and webhook logic
│   └── utils/          # Logger and helper functions
├── knowledge_base.md   # The "source of truth" for Jesse's info
├── webhook.py          # Flask entry point for Render/Cloud Run
└── requirements.txt    # Project dependencies

