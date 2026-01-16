import os
from flask import Blueprint, request
from telebot.types import Update
from src.telegram.bot import bot
from src.utils.logger import setup_logger

logger = setup_logger("webhook")
webhook_bp = Blueprint("webhook", __name__)

RENDER_URL = os.environ.get("RENDER_EXTERNAL_URL") 

@webhook_bp.route("/webhook", methods=["POST"])
def webhook():
    if request.headers.get('content-type') == 'application/json':
        json_string = request.get_data().decode('utf-8')
        update = Update.de_json(json_string)
        bot.process_new_updates([update])
        return '', 200
    else:
        return "Unsupported Media Type", 415

# Helper to configure Telegram to use this endpoint
def setup_webhook():
    base_url = os.environ.get("RENDER_EXTERNAL_URL", "").rstrip("/")

    if base_url:
        webhook_url = f"{RENDER_URL}/webhook"
        bot.remove_webhook() # Clear old settings
        bot.set_webhook(url=webhook_url)
        logger.info(f"Webhook set to: {webhook_url}")
    else:
        logger.warning("RENDER_EXTERNAL_URL not set. Webhook NOT configured.")