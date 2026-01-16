from flask import Blueprint, request
from telebot.types import Update
from src.telegram.bot import bot
from src.utils.logger import setup_logger

logger = setup_logger("webhook")
webhook_bp = Blueprint("webhook", __name__)

@webhook_bp.route("/webhook", methods=["POST"])
def webhook():
    try:
        json_data = request.get_json(force=True)

        chat_id = json_data["message"]["chat"]["id"]
        message = json_data["message"]["text"]
        logger.info(f"Received message from {chat_id}: {message}")

        update = Update.de_json(json_data)
        bot.process_new_updates([update])
        return "OK", 200
    
    except Exception:
        logger.exception("Webhook processing failed.")
        return "ERROR", 500