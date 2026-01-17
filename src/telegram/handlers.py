import os
from random import choice
from src.telegram.bot import bot
from src.rag.llm import query_llm
from src.utils.logger import setup_logger

logger = setup_logger()
PHOTO_DIR = "assets/" 

def safe_text(text: str) -> str:
    return text.encode('utf-8', errors='ignore').decode('utf-8')

# Handlers
@bot.message_handler(commands=['start', 'help'])
def start_message(message):
    bot.reply_to(message, "👋 Hello! I'm **JesseBot**. I'm here to answer anything about Jesse Mokolo.\n\nType /chat to start, or /info to learn more about me!", parse_mode='Markdown')

@bot.message_handler(commands=['chat', 'ask'])
def chat_command(message):
    bot.reply_to(message, "💬 **Chat mode activated!**\nAsk me anything about Jesse (or type 'exit' to stop).", parse_mode='Markdown')
    bot.register_next_step_handler(message, process_chat)

def process_chat(message):
    try:
        user_message = message.text
        if not user_message: return

        # Exit conditions
        if user_message.lower() in ["stop", "/stop", "exit", "quit"]:
            bot.reply_to(message, "👋 Chat mode exited. See you later!")
            return

        # Show 'typing' action so user knows LLM is working
        bot.send_chat_action(message.chat.id, 'typing')

        # RAG Pipeline
        answer = query_llm(user_message)
        bot.send_message(message.chat.id, safe_text(answer))

        logger.info(f"User: {user_message} -> Bot Success")
        
        # Loop back to keep the conversation going
        bot.register_next_step_handler(message, process_chat)

    except Exception as e:
        logger.exception("Error in process_chat")
        bot.reply_to(message, "⚠️ My brain stalled for a second. Try asking again!")

@bot.message_handler(commands=['me'])
def send_jesse_photo(message):
    try:
        # 1. Check if directory exists
        if not os.path.exists(PHOTO_DIR) or not os.listdir(PHOTO_DIR):
            bot.reply_to(message, "❌ No photos found in the assets folder!")
            return

        # 2. Pick a random file and create the FULL path
        random_file = choice(os.listdir(PHOTO_DIR))
        full_path = os.path.join(PHOTO_DIR, random_file)

        bot.send_chat_action(message.chat.id, 'upload_photo')

        with open(full_path, 'rb') as photo:
            bot.send_photo(
                message.chat.id,
                photo,
                caption="Surpriseee! Jesse has always looked stunning, hasn't he? 📸"
            )
        logger.info(f"Sent photo: {full_path}")
    
    except Exception as e:
        logger.error(f"Photo error: {e}")
        bot.reply_to(message, "⚠️ I tried to take a photo, but the lens cap was on!")

@bot.message_handler(commands=['db_status'])
def check_db(message):
    try:
        from src.rag.vectorstore import get_vectorstore
        vs = get_vectorstore()
        count = vs._collection.count() 
        bot.reply_to(message, f"📊 **Database Status**\nChunks indexed: `{count}`", parse_mode='Markdown')
    except Exception as e:
        bot.reply_to(message, f"❌ DB Error: {str(e)}")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "I only answer specific questions in **Chat Mode**. Type /chat to begin!")