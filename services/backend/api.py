import time
import hashlib
import hmac
from urllib.parse import parse_qs, unquote
import asyncio
import logging

from fastapi import FastAPI, APIRouter, status
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

import config
from main import bot
from services.backend.config import TELEGRAM_BOT_TOKEN

app = FastAPI()
api_router = APIRouter()
logging.basicConfig(level=logging.INFO)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ValidationResponse(BaseModel):
    isValid: bool


async def validate_telegram_data(init_data: str) -> bool:
    """
    Проверяет данные initData, полученные от Telegram Mini App.

    :param init_data: Строка query string из Telegram.WebApp.initData.
    :param TELEGRAM_BOT_TOKEN: Токен вашего Telegram-бота.
    :return: True, если данные валидны, иначе False.
    """
    # Разбираем строку init_data в словарь
    data = parse_qs(init_data)

    # Извлекаем hash и удаляем его из данных для проверки
    hash_value = data.pop('hash')[0]

    # Проверяем поле auth_date, чтобы убедиться, что данные не устарели
    auth_date = int(data['auth_date'][0])
    if time.time() - auth_date > 3600:  # Проверяем, что данные не старше 1 часа
        return False

    # Создаем строку data-check
    sorted_items = sorted(data.items())
    data_check_string = '\n'.join(f"{key}={unquote(value[0])}" for key, value in sorted_items)

    # Генерируем секретный ключ с использованием HMAC-SHA256
    secret_key = hmac.new(b"WebAppData", TELEGRAM_BOT_TOKEN.encode(), hashlib.sha256).digest()

    # Вычисляем HMAC-SHA256 для строки data-check с использованием секретного ключа
    calculated_hash = hmac.new(secret_key, data_check_string.encode(), hashlib.sha256).hexdigest()

    # Сравниваем вычисленный хэш с полученным хэшем
    return calculated_hash == hash_value


class InitDataRequest(BaseModel):
    initData: str


@api_router.post("/api/validate_init_data", response_model=ValidationResponse)
async def validate_init_data_endpoint(request: InitDataRequest):
    logging.info(request)
    is_valid = await validate_telegram_data(request.initData)
    if is_valid:
        message = "Данные валидны."
    else:
        message = "Данные не валидны."
    asyncio.create_task(bot.send_message(chat_id=int(config.ADMIN_TELEGRAM_ID), text=message))
    return ValidationResponse(isValid=is_valid)


class DataModel(BaseModel):
    data: str


@api_router.post("/api/send_data", status_code=status.HTTP_204_NO_CONTENT)
async def send_data(data: DataModel):
    logging.info(data)
    message = 'Всё хорошо.'
    asyncio.create_task(bot.send_message(chat_id=int(config.ADMIN_TELEGRAM_ID), text=message))


app.include_router(api_router)

