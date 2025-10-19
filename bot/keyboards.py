from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🛒 Buyurtma berish"), KeyboardButton(text="📞 Aloqa")]
    ],
    resize_keyboard=True
)

inline_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🌐 Saytga o'tish", url="https://ictacademy.uz"),
            InlineKeyboardButton(text="✅ Qo‘shilish", callback_data="join")
        ]
    ]
)

