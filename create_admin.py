# Абсолютно не нужный файл 
from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text 
from create_bot import dp 


# тут будут временно сохраняться одноразовые ключи для того чтобы стать админом 
CODE_FOR_CREATE = ['123']

#словарь со списком админов, id - information about admin (name, age, job_title, phone_number, email)
ADMINS = {}

class FSMAdmin(StatesGroup):
    checking = State()
    photo = State()
    first_name = State()
    last_name = State()
    age = State()
    phone_number = State()
    admin_email = State()
    specialization = State()
    department = State()
    job_title = State() 


# Отмена действия
async def cancel_work(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await message.reply('Cancel work')
    await state.finish()

        

#Start creating admin
async def new_admin(message: types.Message):
    await message.answer('Enter your code') 

async def checking_code(message: types.Message):
    if message.text in CODE_FOR_CREATE:
        await message.answer('Load photo')
        await FSMAdmin.next()
    else:
        print('error') # вывод ошибки в консоль
        await message.answer('Wrong code. Try again!')

async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
    await FSMAdmin.next()
    await message.reply('Enter first name')

async def add_first_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['first_name'] = message.text
    await FSMAdmin.next()
    await message.reply('Enter last name')

async def add_last_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['last_name'] = message.text
    await FSMAdmin.next()
    await message.reply('Enter age')

async def add_age(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['age'] = int(message.text)
    await FSMAdmin.next()
    await message.reply('Enter phone number')

async def add_phone_number(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['phone_number'] = message.text
    await FSMAdmin.next()
    await message.reply('Enter email')

async def add_email(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['email'] = message.text
    await FSMAdmin.next()
    await message.reply('Enter specializations')
    
async def add_specializations(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['specializations'] = message.text
    await FSMAdmin.next()
    await message.reply('Enter department')

async def add_department(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['department'] = message.text
    await FSMAdmin.next()
    await message.reply('Enter job title')

async def add_job_title(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['job_title'] = message.text

    async with state.proxy() as data:
        await message.answer(data)
    await state.finish()


def register_handlers_for_create_admin(dp: Dispatcher):
    # Отмена действия
    dp.register_message_handler(cancel_work, state="*", commands=['cancel'])
    dp.register_message_handler(cancel_work, Text(equals='cancel', ignore_case = True), state="*")

    #Create admin
    dp.register_message_handler(new_admin, commands='new_admin', state=None)
    dp.register_message_handler(checking_code, state=FSMAdmin.checking)
    dp.register_message_handler(load_photo, content_types=['photo'], state=FSMAdmin.photo)
    dp.register_message_handler(add_first_name, state=FSMAdmin.first_name)
    dp.register_message_handler(add_last_name, state=FSMAdmin.last_name)
    dp.register_message_handler(add_age, state=FSMAdmin.age)
    dp.register_message_handler(add_phone_number, state=FSMAdmin.phone_number)
    dp.register_message_handler(add_email, state=FSMAdmin.admin_email)
    dp.register_message_handler(add_specializations, state=FSMAdmin.specialization)
    dp.register_message_handler(add_department, state = FSMAdmin.department)
    dp.register_message_handler(add_job_title, state=FSMAdmin.job_title)