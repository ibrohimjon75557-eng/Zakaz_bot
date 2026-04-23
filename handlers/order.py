from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove
from loader import dp, bot
from states.order_state import OrderState
from keyboards.contact import phone_kb
from config import ADMIN_ID
from db import save_order

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Salom!\n/zakazni bosing.")

@dp.message_handler(commands=['zakazni'])
async def zakazni(message: types.Message):
    await message.answer("📞 Raqamingizni yuboring:", reply_markup=phone_kb)
    await OrderState.phone.set()

@dp.message_handler(content_types=types.ContentType.CONTACT, state=OrderState.phone)
async def get_phone(message: types.Message, state: FSMContext):
    await state.update_data(phone=message.contact.phone_number)
    await message.answer("⚖️ Necha kg?", reply_markup=ReplyKeyboardRemove())
    await OrderState.kg.set()

@dp.message_handler(state=OrderState.phone)
async def wrong_phone(message: types.Message):
    await message.answer("❗ Tugma orqali yuboring")

@dp.message_handler(state=OrderState.kg)
async def get_kg(message: types.Message, state: FSMContext):
    try:
        kg = float(message.text)
        await state.update_data(kg=kg)
        await message.answer("📦 Nechta karobka?")
        await OrderState.box.set()
    except:
        await message.answer("❗ Son kiriting")

@dp.message_handler(state=OrderState.box)
async def get_box(message: types.Message, state: FSMContext):
    try:
        box = int(message.text)
        data = await state.get_data()

        await save_order(
            message.from_user.id,
            data['phone'],
            data['kg'],
            box
        )

        text = f"""
🆕 Yangi zakaz
👤 ID: {message.from_user.id}
📞 {data['phone']}
⚖️ {data['kg']} kg
📦 {box} dona
"""
        await bot.send_message(ADMIN_ID, text)
        await message.answer("✅ Qabul qilindi")

        await state.finish()
    except:
        await message.answer("❗ Butun son yozing")
