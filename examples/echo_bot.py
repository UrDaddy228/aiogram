"""
This is a echo bot.
It echoes any incoming text messages.
"""

import logging
import random

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '1651360931:AAH1wDUZ24PAQNwIKrcyxXI1QLqnQADAkK8'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Привет ;)")


@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    if message.text.lower() == 'шо там ?':
        answer = '@oriffovsh'
        nxt = 'a'
        for i in range(random.randint(1,15)):
            answer += nxt
            nxt = 'x' if nxt == 'a' else 'a'
        if random.randint(0,1):
            answer = answer.upper()
        await message.answer(answer)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
