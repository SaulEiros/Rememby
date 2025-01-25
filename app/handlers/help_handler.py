from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

from app.logger import getLogger

LOG = getLogger(__name__)

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    LOG.info(
       f"User {user.username or user.id} requested help." 
    )

    await update.message.reply_text(
        "Comandos disponibles:\n"
        "/remind - Crear un nuevo recordatorio.\n"
    )

help_handler = CommandHandler("help", help)