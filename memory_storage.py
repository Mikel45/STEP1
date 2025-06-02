from aiogram.fsm.state import StatesGroup, State


class UserState(StatesGroup):
    name = State()
    age = State()
    favorite_programming_language = State()



class SurveyState(StatesGroup):
    experience = State()
    technology = State()



USER_DATA = dict()