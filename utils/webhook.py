import requests

TELEGRAM_BOT_TOKEN = "YOUR_TELEGRAM_TOKEN"
BOT_URL = "YOUR_PUBLIC_URL"  # Reemplaza con tu URL pública
WEBHOOK_URL = f"{BOT_URL}/{TELEGRAM_BOT_TOKEN}"

response = requests.get(f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/setWebhook?url={WEBHOOK_URL}")
print(response.json())

response = requests.get(f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/getWebhookInfo")
print(response.json())
