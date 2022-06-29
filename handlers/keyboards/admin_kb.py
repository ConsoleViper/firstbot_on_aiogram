from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton('/add_employee')
b2 = KeyboardButton('/delete_employee')
b3 = KeyboardButton('/updata_team')
b4 = KeyboardButton('/all_employees')

kb_admin = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

kb_admin.add(b1).add(b2).add(b3).add(b4)

