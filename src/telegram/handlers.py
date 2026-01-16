import os, random
from src.telegram.bot import bot
from src.rag.llm import query_llm
from src.utils.logger import setup_logger

logger = setup_logger()
PHOTO_PATH = "assets/image{}.jpg"

# /start - Start the bot
@bot.message_handler(commands=['start', 'help'])
def start_message(message):
    bot.reply_to(message, "Hello! I'm jmoksbot. I was built to answer questions about Jesse. Type /chat or /ask to start chatting!")

# /chat - Start chatting with JesseBot
@bot.message_handler(commands=['chat', 'ask'])
def chat(message):
    bot.reply_to(message, "Chat mode activated! What would you like to know?")
    bot.register_next_step_handler(message, process_chat)

def process_chat(message):
    def safe_text(text: str) -> str:
        return text.encode('utf-8', errors='ignore').decode('utf-8')

    try:
        user_message = message.text

        # If user wants to exit chat mode
        if user_message.lower() in ["stop", "/stop", "exit", "quit"]:
            bot.reply_to(message, "Chat mode exited.")
            return

        # RAG Pipeline begins
        answer = query_llm(user_message)
        safe_answer = safe_text(answer)

        bot.send_message(message.chat.id, safe_answer)

        logger.info(f"User: {user_message} -> Bot: {safe_answer}")
        
        # Wait for the next message again
        bot.register_next_step_handler(message, process_chat)

    except Exception as e:
        logger.exception("Error processing chat message: %s", str(e))
        bot.reply_to(message, "Sorry, something went wrong while processing your request.")

# /info - About JesseBot
@bot.message_handler(commands=['info', 'about'])
def send_about_info(message):
    about_text = (
        "🤖 **JesseBot v1.0**\n"
        "I am an AI assistant built to represent Jesse Mokolo.\n\n"
        "📍 **Background:** Software Engineer (Babcock University '26).\n"
        "💻 **Expertise:** AI, Python, Web/Backend.\n"
        "🎓 **Status:** First Class honors student.\n\n"
        "Use /chat to ask me anything specific about Jesse's life or career!"
    )
    bot.reply_to(message, about_text, parse_mode='Markdown')

# /reset - Reset the chat context
def reset_handler(message):
    bot.clear_step_handler_by_chat_id(chat_id=message.chat.id)
    bot.reply_to(message, "🔄 Conversation state has been reset. You are now in the main menu. Type /chat to start again.")

# /me - Return image of Jesse
@bot.message_handler(commands=['me'])
def send_jesse_photo(message):
    try:
        if not os.path.exists(PHOTO_PATH):
            bot.reply_to(message, "❌ I couldn't find Jesse's photo in my database!")
            return
        
        bot.send_chat_action(message.chat.id, 'upload_photo')

        with open(PHOTO_PATH.format(str(random.choice([1, 2, 3]))), 'rb') as photo:
            bot.send_photo(
                message.chat.id,
                photo,
                caption="Surpriseee. Jesse has always looked stunning, hasn't he! 📸",
            )
        
        logger.info(f"Sent photo to user {message.chat.id}")
    
    except Exception as e:
        logger.error(f"Error sending photo: {e}")
        bot.reply_to(message, "⚠️ Sorry, I had trouble finding my camera!")

    
# Simple echo handler
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"You said: {message.text}. Type /chat to start a conversation with me about Jesse.")
