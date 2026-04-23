import logging
from aiogram.utils import executor
from loader import dp
from db import create_db

import handlers.order  # MUHIM

logging.basicConfig(level=logging.INFO)

async def on_startup(dispatcher):
    await create_db()

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
