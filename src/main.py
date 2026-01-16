import os
from flask import Flask
from src.telegram.bot import bot
from src.telegram import handlers  
from src.utils.logger import setup_logger
from src.config import PORT
from src.webhook import webhook_bp
from src.pipelines.build_index import build_index

logger = setup_logger()

app = Flask(__name__)
app.register_blueprint(webhook_bp)

@app.route("/", methods=["GET"])
def health():
    return "JesseBot is online and healthy.", 200

if __name__ == "__main__":
    try:
        logger.info("Starting knowledge base indexing...")
        build_index()
        logger.info("Indexing complete. Bot is ready.")
    except Exception as e:
        logger.error(f"Failed to index knowledge base: {e}")

    logger.info(f"Starting Flask app for webhook on port {PORT}...")
    app.run(host='0.0.0.0', port=PORT)