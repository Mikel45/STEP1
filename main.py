import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message

API_TOKEN = ""


dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer("Hello, I'm BOT")


@dp.message()
async def echo_handler(message: Message) -> None:
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer(text="Error occurred")
    finally:
        logging.info(f"Message from {message.from_user.username}({message.from_user.full_name}): {message.text}")


async def main() -> None:
    bot = Bot(token=API_TOKEN)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO,
        stream=sys.stdout,
    )
    asyncio.run(main())
