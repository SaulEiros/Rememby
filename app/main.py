import os
from dotenv import load_dotenv
from fastapi import FastAPI, Request
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

from app.handlers.start_handler import start_handler
from app.handlers.help_handler import help_handler
from app.handlers.remind_handler import remind_handler
from app.logger import getLogger
from app.scheduler import load_reminders, scheduler

LOG = getLogger(__name__)

# Load .env file
load_dotenv()
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Initializate FastAPI and Telegram bot
app = FastAPI()
application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()


# Handle unknown commands
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    LOG.info(f"Received unknown command: {update.message.text}")
    await update.message.reply_text("¡No entiendo ese comando! Usa /ayuda para ver los comandos disponibles.")

# Known Handlers
application.add_handler(start_handler)
application.add_handler(help_handler)
application.add_handler(remind_handler)
application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

# Server Startup
@app.on_event("startup")
async def startup_event():
    await application.initialize()
    await application.start()

    load_reminders(application)
    scheduler.start()

# Server Shutdown
@app.on_event("shutdown")
async def shutdown_event():
    await application.stop()

# Telegram Webhook Endpoint
@app.post(f"/{TELEGRAM_BOT_TOKEN}")
async def webhook(request: Request):
    json_update = await request.json()
    update = Update.de_json(json_update, application.bot)
    await application.process_update(update)
    return {"status": "ok"}

# Health Check
@app.get("/")
async def index():
    return {"message": "Bot de Telegram funcionando"}
