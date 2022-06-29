from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from aiogram import types, Dispatcher
from data_base import posgre_db
from create_bot import dp, bot
from handlers.keyboards import admin_kb

class Employee(StatesGroup):
    photo = State()
    first_name = State()
    last_name = State()
    age = State()
    phone_number = State()
    employee_email = State()
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

# Admin check
async def admin_check(message: types.Message):
    global ID
    ID = message.from_user.id
    await bot.send_message(message.from_user.id,'Проверка пройдена!', reply_markup=admin_kb.kb_admin) # admin keyboard 
    await message.delete()

#Первичная функция сотрудника 
async def new_employee(message: types.Message):
    if message.from_user.id == ID:
        await Employee.photo.set()
        await message.reply('Load photo')

#Добавление фото
async def load_photo(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['photo'] = message.photo[0].file_id
        await Employee.next()
        await message.reply('Enter first name')

#Добавление имени
async def add_first_name(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['first_name'] = message.text
        await Employee.next()
        await message.reply('Enter last name')

#Добавление фамилии
async def add_last_name(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['last_name'] = message.text
        await Employee.next()
        await message.reply('Enter age')

#Добавление возраста
async def add_age(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['age'] = int(message.text)
        await Employee.next()
        await message.reply('Enter phone number')

#Добавление phone number
async def add_phone_number(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['phone_number'] = message.text
        await Employee.next()
        await message.reply('Enter email')

#Добавление email
async def add_employee_email(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['email'] = message.text
        await Employee.next()
        await message.reply('Enter specialization')

#add specialize
async def add_specialization(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['specialization'] = message.text
        await Employee.next()
        await message.reply('Enter department')

# add department
async def add_department(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['department'] = message.text 
        await Employee.next()
        await message.reply('Enter job title')

# add job_title
async def add_job_title(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['job_title'] = message.text
    
    await posgre_db.add_employee_in_table(state)
    await state.finish()

# Просмотр сотрудников
async def watching_employees(message: types.Message):
    await posgre_db.sql_read(message)

#? Удаление сотрудника
async def remove_employee(message: types.Message):
    await message.answer('Сотрудник удален')

#? Перевод сотрудника вдругой отдел
async def move_employee(message: types.Message):
    await message.answer('Сотрудник переведен')

def register_handlers_admin(dp : Dispatcher):
    
    # Отмена действия
    dp.register_message_handler(cancel_work, state="*", commands=['cancel'])
    dp.register_message_handler(cancel_work, Text(equals='cancel', ignore_case = True), state="*")
    
    #Проверка на админа
    dp.register_message_handler(admin_check, commands=['admin'], is_chat_admin = True)
    
    # Добавление нового сотрудника 
    dp.register_message_handler(new_employee, commands=['add_employee'], state=None)
    dp.register_message_handler(load_photo, content_types=['photo'], state=Employee.photo)
    dp.register_message_handler(add_first_name, state=Employee.first_name)
    dp.register_message_handler(add_last_name, state=Employee.last_name)
    dp.register_message_handler(add_age, state=Employee.age)
    dp.register_message_handler(add_phone_number, state=Employee.phone_number)
    dp.register_message_handler(add_employee_email, state=Employee.employee_email)
    dp.register_message_handler(add_specialization, state=Employee.specialization)
    dp.register_message_handler(add_department, state=Employee.department)
    dp.register_message_handler(add_job_title, state=Employee.job_title)

    # Просмотр сотрудников
    dp.register_message_handler(watching_employees, commands=['all_employees'])

    #? in process to create
    dp.register_message_handler(remove_employee, commands=['Remove_employee'])
    dp.register_message_handler(move_employee, commands=['Move_employee'])
