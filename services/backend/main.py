import asyncio
import logging
import json
from typing import Any, Callable, Dict, Awaitable
import threading
import uvicorn

from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram import Bot, Dispatcher, Router, F, BaseMiddleware
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo, WebAppData, TelegramObject, ContentType, KeyboardButton
from aiogram.filters import CommandStart, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.enums.parse_mode import ParseMode

from config import TELEGRAM_BOT_TOKEN, WEBAPP_URL


bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher()
router = Router()
webapp_url = WEBAPP_URL
# webapp_url_test = 'https://mishachza.github.io/telegram-webapp-example-barbershop/'


@dp.message(CommandStart(), StateFilter('*'))
async def get_start(message: Message, state: FSMContext):
    await state.clear()
    webapp = [[InlineKeyboardButton(text=f'Оплатить', web_app=WebAppInfo(url=webapp_url))]]
    keyboard = InlineKeyboardMarkup(inline_keyboard=webapp)
    await message.answer('Записаться можно нажав кнопку.', reply_markup=keyboard)

    # builder = ReplyKeyboardBuilder()
    # builder.add(KeyboardButton(text='Отправить данные', web_app=WebAppInfo(url=webapp_url)))
    # await message.answer(text='Привет!', reply_markup=builder.as_markup())

@dp.message(F.content_type == ContentType.WEB_APP_DATA)
async def parse_data(message: Message):
    print(message)
    data = json.loads(message.web_app_data.data)
    print(data)


class CheckUserMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any],
    ) -> Any:
        logging.info(f"Получено событие: {event}")


async def main():
    # dp.message.middleware.register(CheckUserMiddleware())
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())