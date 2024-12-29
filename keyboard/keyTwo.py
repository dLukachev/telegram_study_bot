from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton 
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

mainMenu = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Ну ладно, уговорил, чертяга:)', callback_data='payment')],
                                                     [InlineKeyboardButton(text='Расскажи о курсе', callback_data='info')],
                                                     [InlineKeyboardButton(text='Расскажи о себе', callback_data='infome')],
                                                     [InlineKeyboardButton(text='А есть отзывы?', callback_data='otz')]])

infoCourse = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Покажи пример дня', callback_data='day')],
                                                     [InlineKeyboardButton(text='Программу курса бы', callback_data='program')],
                                                     [InlineKeyboardButton(text='Обратно', callback_data='otv5')]])

infoDay = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Программу курса бы', callback_data='program')],
                                                     [InlineKeyboardButton(text='Обратно', callback_data='otv5')]])

infoProgram = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Покажи пример дня', callback_data='day')],
                                                     [InlineKeyboardButton(text='Обратно', callback_data='otv5')]])

moreOtz = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Давай еще!', callback_data='moreOtz')],
                                                     [InlineKeyboardButton(text='Обратно', callback_data='otv5')]])

back = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Обратно', callback_data='otv5')]])

go = ReplyKeyboardMarkup(resize_keyboard=True, 
                                    one_time_keyboard=True, keyboard=[[KeyboardButton(text='Давай учиться уже!')]])