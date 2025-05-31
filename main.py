import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher

from STEP1.handlers import echo, common, form, menu
from STEP1.settings import API_TOKEN


async def main() -> None:
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO,
        stream=sys.stdout,
    )
    dp = Dispatcher()
    bot = Bot(token=API_TOKEN)
    dp.include_router(common.router)
    dp.include_router(form.router)
    dp.include_router(menu.router)
    dp.include_router(echo.router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
