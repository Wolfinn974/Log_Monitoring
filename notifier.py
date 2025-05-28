import os
import requests
from dotenv import load_dotenv

load_dotenv("/home/wolf/Desktop/cyberprojects/siemlike/.env")

TOKEN= os.getenv("TELEGRAM_TOKEN")
CHAT_ID= os.getenv("TELEGRAM_CHAT_ID")

def send_telegram_alert(message):
    if not TOKEN or not CHAT_ID:
        print("[X] Token or ID missing")
        return
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": message
    }

    try:
        response = requests.post(url, data=data)
        if response.status_code != 200:
            print(f"[X]Telegram Error: {response.text}")
    except Exception as e:
        print(f"[X] Telegram exception: {e}")