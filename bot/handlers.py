from aiogram import types, Router, F
from aiogram.fsm.context import FSMContext
from .keyboards import main_menu, inline_menu
from .states import OrderState

router = Router()

@router.message(F.text == "/start")
async def start_cmd(message: types.Message):
    await message.answer("Salom! Men mini SaaS botman 😎", reply_markup=main_menu)

@router.message(F.text == "🛒 Buyurtma berish")
async def start_order(message: types.Message, state: FSMContext):
    await message.answer("Ismingizni kiriting:")
    await state.set_state(OrderState.waiting_for_name)

@router.message(OrderState.waiting_for_name)
async def ask_phone(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Telefon raqamingizni kiriting:")
    await state.set_state(OrderState.waiting_for_phone)

@router.message(OrderState.waiting_for_phone)
async def finish_order(message: types.Message, state: FSMContext):
    data = await state.get_data()
    name = data["name"]
    phone = message.text
    await message.answer(f"✅ Buyurtma qabul qilindi!\n👤 {name}\n📞 {phone}", reply_markup=inline_menu)
    await state.clear()

@router.callback_query(F.data == "join")
async def join_callback(callback: types.CallbackQuery):
    await callback.message.answer("🎉 Tabriklaymiz! Siz muvaffaqiyatli qo‘shildingiz.")
    await callback.answer()

