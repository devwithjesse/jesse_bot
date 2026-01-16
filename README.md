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
```

---

## ⚙️ Setup & Installation

Follow these steps to get your local environment ready for JesseBot.

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/JesseBot.git
cd JesseBot

```

### 2. Environment Setup

Create a virtual environment to manage your dependencies cleanly:

```bash
python -m venv .venv

# On Windows:
.venv\Scripts\activate

# On Mac/Linux:
source .venv/bin/activate

```

### 3. Install Dependencies

```bash
pip install -r requirements.txt

```

### 4. Configuration

Create a `.env` file in the root directory and add your credentials:

```bash
TELEGRAM_BOT_TOKEN=your_telegram_token
GEMINI_API_KEY=your_gemini_key
GROQ_API_KEY=your_groq_key
HF_TOKEN=your_huggingface_token
PORT=5000

```

---

## 🔑 How to Get Your API Keys

### 1. Telegram Bot Token

1. Open the Telegram app and search for **@BotFather**.
2. Start a chat and send the command `/newbot`.
3. Follow the prompts to name your bot and choose a username (must end in `bot`).
4. BotFather will provide a unique **API Token**. Copy this into your `.env` file.

### 2. Google Gemini API Key

1. Visit [Google AI Studio](https://aistudio.google.com/).
2. Sign in with your Google account.
3. Click on the **"Get API key"** button in the sidebar.
4. Click **"Create API key"** and select a project (or create a new one).
5. Copy the generated key.

### 3. Groq API Key (Fallback LLM)

1. Go to the [Groq Cloud Console](https://console.groq.com/).
2. Log in or sign up for an account.
3. Navigate to the **"API Keys"** section on the left sidebar.
4. Click **"Create API Key"**, give it a name (e.g., `JesseBot_Fallback`), and copy the key immediately.

### 4. Hugging Face Token (Embeddings)

1. Log in to [Hugging Face](https://huggingface.co/).
2. Click on your profile picture in the top right and go to **Settings**.
3. Select **"Access Tokens"** from the left-hand menu.
4. Click **"New token"**.
5. Give it a name and set the type to **"Read"**.
6. Copy the token.

---

## 🏃 Running the Bot Locally

Once your `.env` file is ready, you can start the bot for local testing:

```bash
python main.py

```

This will initialize the knowledge base (build the Chroma index) and start the Flask server. To receive messages locally, you may need a tool like **ngrok** to tunnel your local port to a public URL for Telegram's webhooks.

---

This setup ensures your bot has the "brains" (Gemini/Groq) and the "memory" (Hugging Face Embeddings) it needs to represent you perfectly!

This [tutorial on setting up Telegram bot APIs](https://www.youtube.com/watch?v=vb3QDWnqtXA) walks through the initial steps with BotFather and basic command handling, which is essential for getting your bot's token and starting your development.
