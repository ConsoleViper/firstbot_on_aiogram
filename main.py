import asyncio
from aiogram import executor
from create_bot import dp
from handlers import admin, employee
from data_base import posgre_db

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


async def workcheck(_):
    print("Bot is working") 
    await posgre_db.sql_start()

admin.register_handlers_admin(dp=dp)

employee.register_handlers_employee(dp = dp)



executor.start_polling(dp, skip_updates=True, on_startup=workcheck)
