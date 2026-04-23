from aiogram.dispatcher.filters.state import State, StatesGroup

class OrderState(StatesGroup):
    phone = State()
    kg = State()
    box = State()
