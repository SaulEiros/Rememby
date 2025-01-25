from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

from app.logger import getLogger

LOG = getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    chat = update.effective_chat

    LOG.info(
       f"User {user.username or user.id} started the application from {chat.type}" 
    )

    await update.message.reply_text("¡Hola! Usa /remind para configurar recordatorios.")

start_handler = CommandHandler("start", start)
