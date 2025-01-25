import os
from fastapi import FastAPI, Request
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters
from dotenv import load_dotenv

from app.handlers.start_handler import start_handler
from app.handlers.help_handler import help_handler
from app.handlers.remind_handler import remind_handler

from app.scheduler import load_reminders, scheduler

# Cargar el token desde .env
load_dotenv()
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Inicializar FastAPI y el bot
app = FastAPI()
application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()


# Manejo de mensajes desconocidos
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("¡No entiendo ese comando! Usa /ayuda para ver los comandos disponibles.")

# Registrar los manejadores
application.add_handler(start_handler)
application.add_handler(help_handler)
application.add_handler(remind_handler)
application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

# Inicializa el bot al iniciar el servidor
@app.on_event("startup")
async def startup_event():
    await application.initialize()
    await application.start()

    load_reminders(application)
    scheduler.start()

# Detiene el bot al cerrar el servidor
@app.on_event("shutdown")
async def shutdown_event():
    await application.stop()

# Endpoint para el webhook
@app.post(f"/{TELEGRAM_BOT_TOKEN}")
async def webhook(request: Request):
    json_update = await request.json()  # Obtén el JSON del mensaje
    update = Update.de_json(json_update, application.bot)  # Convierte el JSON en un objeto Update
    await application.process_update(update)  # Procesa la actualización
    return {"status": "ok"}

# Endpoint de prueba
@app.get("/")
async def index():
    return {"message": "Bot de Telegram funcionando"}
