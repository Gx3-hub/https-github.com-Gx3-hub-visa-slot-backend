import json
import requests

# Load configuration from config.json
with open("config.json") as f:
    config = json.load(f)

# Telegram Bot API setup
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

# Notify when bot starts
send_telegram_message("Visa slot bot is live and ready to notify you!")

# ---- SIMULATED LOGIC TO CHECK APPOINTMENTS ----
# Replace this block with real appointment-checking code
appointment_available = True  # Simulating that a slot was found

if appointment_available: 
    send_telegram_message("**Visa Appointment Slot Available!** Visit the CGI website now to book it.")
