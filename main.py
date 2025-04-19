import json
import requests
from datetime import datetime

# Load configuration from config.json
with open("config.json") as f:
    config = json.load(f)

# Extract Telegram config
bot_token = config.get("telegram_bot_token")
chat_id = config.get("telegram_user_id")

def send_telegram_message(text):
    if bot_token and chat_id:
        send_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        response = requests.post(send_url, data={"chat_id": chat_id, "text": text})
        if response.status_code == 200:
            print("Telegram message sent successfully.")
        else:
            print("Failed to send Telegram message:", response.text)
    else:
        print("Telegram bot token or chat ID missing in config.json")

# Notify that the bot has started
send_telegram_message("Visa slot bot is live and ready to notify you!")

# Simulated slot availability check (replace this with real scraping logic)
appointment_available = True
slot_date_str = "2025-06-15"  # <-- this should be dynamically extracted from the website

if appointment_available:
    slot_date = datetime.strptime(slot_date_str, "%Y-%m-%d")
    start_date = datetime.strptime("2025-04-01", "%Y-%m-%d")
    end_date = datetime.strptime("2025-08-31", "%Y-%m-%d")

    if start_date <= slot_date <= end_date:
        send_telegram_message(f"Slot available: {slot_date_str}")
    else:
        print(f"Slot {slot_date_str} is outside your preferred range.")
