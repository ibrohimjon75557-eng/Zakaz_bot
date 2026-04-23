from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

phone_kb = ReplyKeyboardMarkup(resize_keyboard=True)
phone_kb.add(KeyboardButton("📱 Raqam yuborish", request_contact=True))
