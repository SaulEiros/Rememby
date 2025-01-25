from apscheduler.schedulers.asyncio import AsyncIOScheduler
from app.database import cursor
from datetime import datetime

scheduler = AsyncIOScheduler()

async def send_reminder(application, job):
    bot = application.bot
    user_id = job['user_id']
    message = job['message']

    await bot.send_message(chat_id=user_id, text=f"Recordatorio: {message}")

def load_reminders(application):
    cursor.execute("SELECT id, user_id, message, reminder_time FROM reminders WHERE reminder_time > datetime('now')")
    reminders = cursor.fetchall()

    for reminder in reminders:
        reminder_id, user_id, message, reminder_time = reminder
        scheduler.add_job(
            send_reminder,
            "date",
            run_date=datetime.strptime(reminder_time, "%Y-%m-%d %H:%M"),
            kwargs={"application": application, "job": {"user_id": user_id, "message": message}}
        )

def add_reminder(application, user_id, message, reminder_time):
    scheduler.add_job(
        send_reminder,
        "date",
        run_date=datetime.strptime(reminder_time, "%Y-%m-%d %H:%M"),
        kwargs={"application": application, "job": {"user_id": user_id, "message": message}}
    )
