import os
from dotenv import load_dotenv


load_dotenv()


TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
ADMIN_TELEGRAM_ID = os.getenv('ADMIN_TELEGRAM_ID')
WEBAPP_URL = os.getenv('WEBAPP_URL')