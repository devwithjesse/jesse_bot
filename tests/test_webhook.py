import unittest
import requests
from src.utils.logger import setup_logger
from src.config import TELEGRAM_BOT_API_TOKEN, TELEGRAM_CHAT_ID, NGROK_TEST_URL

logger = setup_logger("test_webhook")

ngrok_url = NGROK_TEST_URL # Replace with your actual ngrok URL
webhook_url = f"{ngrok_url}/webhook"

class TestWebhook(unittest.TestCase):
    def test_set_webhook(self):
        """Test that Telegram can set the webhook URL correctly."""

        response = requests.get(
            f"https://api.telegram.org/bot{TELEGRAM_BOT_API_TOKEN}/setWebhook",
            params={"url": webhook_url}
        )

        data = response.json()
        logger.info(f"Set webhook response: {data}")

        self.assertTrue(data.get("ok"), "Failed to set webhook")

    def test_get_webhook_info(self):
        """Test that Telegram webhook info is retrievable."""

        response = requests.get(
            f"https://api.telegram.org/bot{TELEGRAM_BOT_API_TOKEN}/getWebhookInfo"
        )

        data = response.json()
        logger.info(f"Get webhook info response: {data}")

        self.assertTrue(data.get("ok"), "Failed to get webhook info")
        self.assertEqual(data["result"]["url"], webhook_url, "Webhook URL does not match")

    def test_dummy_message(self):
        """Test sending a dummy message to bot (requires running bot locally"""

        TEST_CHAT_ID = TELEGRAM_CHAT_ID  # Replace with a valid chat ID for testing
        TEST_TEXT = "Hello from webhook test!"

        # Send message using Telegram API
        response = requests.get(
            f"https://api.telegram.org/bot{TELEGRAM_BOT_API_TOKEN}/sendMessage",
            params={"chat_id": TEST_CHAT_ID, "text": TEST_TEXT}
        )

        data = response.json()
        logger.info(f"Send message response: {data}")

        self.assertTrue(data.get("ok"), "Failed to send test message")

    
if __name__ == "__main__":
    unittest.main()