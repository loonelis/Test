import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart, or_f
from handlers.user_private import user_private_router
from handlers.user_group import user_group_router
from common.bot_cmds_list import private

ALLOWED_UPDATES = ['message, edited_message']

bot = Bot(token="7041737904:AAHPiCA4Pxz3esklZX7gI8vcYNS8qKIqzYo")
dp = Dispatcher()


dp.include_routers(
 user_private_router, 
 user_group_router, 
 )


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    # await bot.delete_my_commands(scope=types.BotCommandScopeAllPrivateChats())
    await bot.set_my_commands(commands=private, scope=types.BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)

asyncio.run(main())