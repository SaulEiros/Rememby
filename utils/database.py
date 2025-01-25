import sqlite3
import os

# Ruta de la base de datos
DB_PATH = os.path.join(os.path.dirname(__file__), "../data/reminders.db")

# Conexión global
conn = sqlite3.connect(DB_PATH, check_same_thread=False)
cursor = conn.cursor()

# Verifica que la tabla está creada
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cursor.fetchall())
