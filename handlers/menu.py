import logging

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

router = Router()

_KEYBOARD = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🐍 Python", callback_data="Python"),
            InlineKeyboardButton(text="💻 Go", callback_data="Go"),
            InlineKeyboardButton(text="🚀 Rust", callback_data="Rust"),
        ],
    ]
)


@router.message(Command(commands=["menu"]))
async def cmd_menu(message: Message) -> None:
    await message.answer("Выберите язык программирования", reply_markup=_KEYBOARD)



@router.callback_query()
async def handle_callback(callback: CallbackQuery):
    data = callback.data
    user = callback.from_user

    await callback.message.answer(f"Ты выбрал язык: {data}")
    logging.info(f"Callback from @{user.username} ({user.id}): {data}")

    await callback.answer()
