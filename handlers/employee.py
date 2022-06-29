from aiogram import types, Dispatcher
from create_bot import dp, bot
from handlers.keyboards import kb_employee

#Просто приветсвие
async def welcomer(message: types.Message):
    await message.answer('Hi\nThis is a bot help to control your company\nSorry, technical work in progress...', reply_markup=kb_employee)

#Проверка должности сотрудника
async def check_position(message: types.Message):
    await message.answer('Ваша должность')

#Проверка зарплаты сотрудника
async def check_salary(message: types.Message):
    await message.answer('Ваша зарплата')

#Просмотр команды сотрудника
async def employee_team(message: types.Message):
    await message.answer('Ваша команда')

def register_handlers_employee(dp : Dispatcher):
    dp.register_message_handler(welcomer, commands=['start', 'help'])
    dp.register_message_handler(check_position, commands=['check_position'])
    dp.register_message_handler(check_salary, commands=['check_salary'])
    dp.register_message_handler(employee_team, commands=['employee_team'])
