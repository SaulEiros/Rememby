from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Comandos disponibles:\n"
        "/remind - Crear un nuevo recordatorio.\n"
    )

help_handler = CommandHandler("help", help)