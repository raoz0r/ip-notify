import os
import socket
import requests
from pathlib import Path
from dotenv import load_dotenv

HERE = Path(__file__).parent
load_dotenv(HERE.parent / ".env.ip_notify")

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID   = os.getenv("CHAT_ID")

def send_telegram(ip: str):
    host = socket.gethostname()
    msg  = f"👻 Host: {host}\\n🌐 IP: {ip}"
    url  = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    resp = requests.post(url, data={"chat_id": CHAT_ID, "text": msg})
    resp.raise_for_status()
