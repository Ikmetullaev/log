from dotenv import load_dotenv
import os

load_dotenv()  # Bu funksiyani chaqirmasang, .env o‘qilmaydi

DB_FILENAME = os.getenv("DB_FILENAME", "log.db")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "maxfiyparol")
SECRET_KEY = os.getenv("SECRET_KEY", "default-secret")
DEBUG = os.getenv("DEBUG", "False").lower() == "true"
