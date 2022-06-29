from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton('/check_position')
b2 = KeyboardButton('/check_salary')
b3 = KeyboardButton('/employee_team')

kb_employee = ReplyKeyboardMarkup(resize_keyboard=True)

kb_employee.add(b1).add(b2).add(b3)
