import json
import requests
from datetime import datetime
from selenium import webdriver

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
        from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import time
import requests

# Your credentials and config
USERNAME = "khaldia belaid"
PASSWORD = "Hs2V9UJ3aPW5R7q"
bot_token = "8014939637:AAGWPXxiusFxdk3KgWQd1Zf3ckFvxEFyiyY"
chat_id = "6093496861"

# Headless Chrome setup
options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

try:
    print("Starting bot...")

    # Step 1: Open login page
    driver.get("https://cgifederal.secure.force.com/")

    # Add login logic here
    # Example placeholder
    print("Logging in...")
    # Simulate login success
    print("Login successful!")

    # Step 2: Navigate to appointment calendar
    print("Navigating to calendar page...")
    driver.get("https://cgifederal.secure.force.com/appointments/calendar")  # Example URL
    time.sleep(3)

    # Save screenshot for confirmation
    driver.save_screenshot("calendar_page.png")
    print("Screenshot saved: calendar_page.png")

    # Step 3: Attempt to find a slot (replace this with actual scraping logic)
    slot_date_str = "2025-06-15"  # Replace this with dynamic scraping
    print(f"Slot found: {slot_date_str}")

    # Step 4: Check if slot is within target range
    slot_date = datetime.strptime(slot_date_str, "%Y-%m-%d")
    start_date = datetime.strptime("2025-04-01", "%Y-%m-%d")
    end_date = datetime.strptime("2025-08-31", "%Y-%m-%d")

    if start_date <= slot_date <= end_date:
        print("Slot is within range. Sending Telegram alert...")
        send_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        response = requests.post(send_url, data={"chat_id": chat_id, "text": f"Slot available: {slot_date_str}"})
        print("Telegram message sent.")
    else:
        print("Slot found, but it's outside your desired range.")

except Exception as e:
    print(f"Error: {e}")

finally:
    driver.quit()


# DEBUGGING SECTION

# Confirm login success
print("Login successful!")

# Confirm calendar page access
print("Navigated to appointment calendar page.")
driver.save_screenshot("calendar_debug_screenshot.png")
print("Screenshot saved as 'calendar_debug_screenshot.png'.")

# Show slot date found
print(f"Slot found (test value): {slot_date_str}")

# Confirm range check
if start_date <= slot_date <= end_date:
    print("Slot is within range.")
else:
    print("Slot is outside the desired date range.")
