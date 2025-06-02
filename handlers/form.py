import logging

from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from memory_storage import UserState, USER_DATA

router = Router()

@router.message(Command("form"))
async def cmd_name(message: Message, state: FSMContext) -> None:
    await message.answer(
        text="Как тебя зовут?"
    )
    await state.set_state(UserState.name)


@router.message(UserState.name)
async def age_choice(message: Message, state: FSMContext) -> None:
    name = message.text.capitalize()
    USER_DATA["name"] = name
    await state.update_data(name=name)
    await message.answer(
        text="Сколько тебе лет?"
    )
    await state.set_state(UserState.age)



@router.message(UserState.age)
async def favorite_programming_language_choice(message: Message, state: FSMContext) -> None:
    age = int(message.text)
    USER_DATA["age"] = age
    await state.update_data(age=age)
    await message.answer(
        text="Какой твой любимый язык программирования?"
    )
    await state.set_state(UserState.favorite_programming_language)


@router.message(UserState.favorite_programming_language)
async def cmd_finish(message: Message, state: FSMContext) -> None:
    language = message.text.capitalize()
    USER_DATA["favorite_programming_language"] = language
    await message.answer(
        text=f"Спасибо! Ты {USER_DATA['name']}, тебе {USER_DATA['age']} лет и ты любишь {USER_DATA['favorite_programming_language']}"
    )
    logging.info(f"Completed form for {message.from_user.username} ({message.from_user.id}): {USER_DATA}")
    await state.clear()




