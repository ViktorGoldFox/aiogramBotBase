from aiogram import Bot, types, Dispatcher

from Core import config
from bot.base.router import base_router

class TelegramBot:
    def __init__(self, token: str):
        self.bot: Bot = Bot(token)
        self.dp = Dispatcher()

    def setup_handlers(self):
        self.dp.include_router(base_router)

    async def on_startup(self):
        self.setup_handlers()
        await self.dp.start_polling(self.bot)

bot = TelegramBot(config.bot.token)