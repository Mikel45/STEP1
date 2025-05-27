from aiogram.fsm.state import StatesGroup, State


class UserState(StatesGroup):
    name = State()
    age = State()
    favorite_programming_language = State()



USER_DATA = dict()