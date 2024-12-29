from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton 
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

mesF = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Кнопка', callback_data='otv')]])

mes1 = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Кнопка1', callback_data='otv1')]])

mes2 = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Кнопка2', callback_data='otv2')]])

mes3 = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Кнопка3', callback_data='otv3')]])

mes4 = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Кнопка4', callback_data='otv4')]])

mes5 = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Кнопка5', callback_data='otv5')]])

mes6 = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Кнопка6', callback_data='otv6')]])

go = ReplyKeyboardMarkup(resize_keyboard=True, 
                                    one_time_keyboard=True, keyboard=[[KeyboardButton(text='Звучит пока интересно..')]])