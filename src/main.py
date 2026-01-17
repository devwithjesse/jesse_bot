import os
from flask import Flask
from src.telegram.bot import bot
from src.telegram import handlers  
from src.utils.logger import setup_logger
from src.config import PORT
from src.webhook import webhook_bp, setup_webhook

# Ensure handlers are imported to register them
handlers

logger = setup_logger()

app = Flask(__name__)
app.register_blueprint(webhook_bp)

@app.route("/", methods=["GET"])
def health():
    return "JesseBot is online and healthy.", 200

with app.app_context():
    setup_webhook()

if __name__ == "__main__":
    logger.info(f"Starting Flask app for webhook on port {PORT}...")
    app.run(host='0.0.0.0', port=PORT)