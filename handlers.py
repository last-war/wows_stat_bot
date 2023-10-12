from aiogram import F, Router, types

from keyboards import keybuild as kb
import text

from aiogram.filters import CommandStart, Command, CommandObject
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import Message

from utils import get_id_by_name


router = Router()


@router.message(F.text == "Меню")
@router.message(F.text == "Вихід")
@router.message(F.text == "◀️ Вихід")
async def menu(message: Message):
    await message.answer(text.menu, reply_markup=kb.menu)


@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    builder = ReplyKeyboardBuilder()
    builder.add(types.KeyboardButton(text="EU"))
    builder.add(types.KeyboardButton(text="NA"))
    builder.add(types.KeyboardButton(text="ASIA"))
    builder.adjust(3)

    await message.answer(f"{text.key_gegion}", reply_markup=builder.as_markup(resize_keyboard=True))


@router.message(Command('stat'))
async def get_my_stat(message: Message, command: CommandObject) -> None:
    """
    This handler receives messages with `/stat` command
    """
    if command.args:
        await message.answer(f" your wows ID:{get_id_by_name(command.args)}")
    else:
        await message.answer(f"Need your game name")


@router.message(F.text.lower() == "EU")
async def with_puree(message: types.Message):

    await message.reply("Виконати реєстрацію", reply_markup=types.ReplyKeyboardRemove())


@router.message(Command('Допомога'))
async def get_my_stat(message: Message) -> None:
    """
    This handler receives messages with `/Допомога` command
    """

    await message.answer(f" send /stat and your wows name")


@router.message()
async def echo_handler(message: types.Message) -> None:
    """
    Handler will forward receive a message back to the sender

    By default, message handler will handle all message types (like a text, photo, sticker etc.)
    """
    try:
        # Send a copy of the received message
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        # But not all the types is supported to be copied so need to handle it
        await message.answer("Nice try!")
