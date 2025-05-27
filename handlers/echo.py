import logging

from aiogram import Router
from aiogram.types import Message

router = Router()

@router.message()
async def echo_handler(message: Message) -> None:
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer(text="Error occurred")
    finally:
        logging.info(f"Message from {message.from_user.username}({message.from_user.id}): {message.text}")