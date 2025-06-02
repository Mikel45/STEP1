from aiogram import Router
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery

from memory_storage import SurveyState

router = Router()

_EXPERIENCE_KEYBOARD = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🔰 Junior", callback_data="Junior"),
            InlineKeyboardButton(text="🔧 Middle", callback_data="Middle"),
            InlineKeyboardButton(text="🧠 Senior", callback_data="Senior"),
        ]
    ]
)


_TECHNOLOGY_KEYBOARD = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🐍 FastAPI", callback_data="FastAPI"),
            InlineKeyboardButton(text="🗃 SQLAlchemy", callback_data="SQLAlchemy"),
            InlineKeyboardButton(text="📦 Redis", callback_data="Redis"),
        ]
    ]
)



@router.message(Command(commands=["survey"]))
async def cmd_survey(message: Message, state: FSMContext) -> None:
    await message.answer("Выбери свой опыт в Python:", reply_markup=_EXPERIENCE_KEYBOARD)
    await state.set_state(SurveyState.experience)


@router.callback_query(StateFilter(SurveyState.experience))
async def handle_experience(callback: CallbackQuery, state: FSMContext):
    data = callback.data

    await state.update_data(experience=data)

    await callback.message.answer("Выбери любимую технологию:", reply_markup=_TECHNOLOGY_KEYBOARD)
    await state.set_state(SurveyState.technology)


@router.callback_query(StateFilter(SurveyState.technology))
async def handle_technology(callback: CallbackQuery, state: FSMContext):
    data = callback.data
    await state.update_data(technology=data)
    user_data = await state.get_data()

    await callback.message.answer(f"Спасибо! Вы: {user_data['experience']}, предпочитаете: {user_data['technology']}")
    await state.clear()