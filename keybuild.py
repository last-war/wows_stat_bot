
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from aiogram.utils.keyboard import InlineKeyboardBuilder



menu = [
    [InlineKeyboardButton(text="🔎 Допомога", callback_data="help")]
]
menu = InlineKeyboardMarkup(inline_keyboard=menu)
exit_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="◀️ Вихід")]], resize_keyboard=True)
iexit_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="◀️ Вихід", callback_data="menu")]])

"""
builder = InlineKeyboardBuilder()
for i in range(15):
    builder.button(text=f"Кнопка {i}", callback_data=f"button_{i}")
builder.adjust(2)
await msg.answer("Текст сообщения", reply_markup=builder.as_markup())
"""
