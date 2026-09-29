from aiogram import Router, F, types
from aiogram.filters import Command, CommandObject

from jokes import getJoke

group_router = Router()
group_router.message.filter(F.chat.type.in_({"group", "supergroup"}))

@group_router.message(Command("joke"))
async def Joke(message: types.Message):
    joke = getJoke()
    if joke != "-1": await message.answer(joke)
    else: await message.reply("Ты крутой")