import logging

from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from memory_storage import USER_DATA

router = Router()

@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer("Hello, I'm BOT")



@router.message(Command(commands=["cancel"]))
@router.message(F.text.lower() == "отмена")
async def cmd_cancel(message: Message, state: FSMContext) -> None:
    await message.answer(
        text="Опрос отменён!"
    )
    await state.clear()
    USER_DATA.clear()