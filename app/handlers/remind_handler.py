from telegram import Update
from telegram.ext import CommandHandler, ContextTypes
from app.database import conn, cursor
from app.scheduler import add_reminder
from datetime import datetime

async def remind(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        user_id = update.effective_user.id
        username = update.effective_user.username
        message = " ".join(context.args[:-1])
        reminder_time = context.args[-1]

        # Validar el formato de la fecha
        reminder_time_parsed = datetime.strptime(reminder_time, "%Y-%m-%d:%H:%M").strftime("%Y-%m-%d %H:%M")

        # Guardar en la base de datos
        cursor.execute(
            "INSERT INTO reminders (user_id, username, message, reminder_time) VALUES (?, ?, ?, ?)",
            (user_id, username, message, reminder_time_parsed)
        )
        conn.commit()

        scheduler = context.application
        add_reminder(scheduler, user_id, message, reminder_time_parsed)
        await update.message.reply_text(f"Recordatorio guardado: '{message}' para el {reminder_time_parsed}.")
    except (IndexError, ValueError):
        await update.message.reply_text("Uso: /remind <mensaje> <YYYY-MM-DD:HH:MM>")

remind_handler = CommandHandler("remind", remind)
