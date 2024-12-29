from aiogram import Router, F
from aiogram.filters import CommandStart, CommandObject, Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from sqlalchemy import select
from database.models import async_session, User, UserPayment


#Это стадия представляет собой расказ истории, а так же обработку спец. ссылок с квери параметром, например: "?start=hfhf"
#Последний обработчик перекидывает пользователя на вторую стадию.

import database.requests as rq
import keyboard.keyOne as kb
import keyboard.keyThree as lkb

oneStage = Router()
class gototwo(StatesGroup):
    gotwo = State()
activate_bot = []


@oneStage.message(CommandStart(deep_link=True))
async def startqwery(message: Message, command: CommandObject, state: FSMContext):
    await rq.setUser(tg_id=message.from_user.id, 
                     username=message.from_user.first_name)    
    async with async_session() as session:
        # Выполнение запроса для получения всех ID пользователей
        result = await session.execute(select(UserPayment.tg_id))
        ids = result.scalars().all()
        global user_id
        user_id = message.from_user.id

        if message.from_user.id in ids:
            await message.answer('Кажется мы уже знакомы...', reply_markup=lkb.lesz)
        elif message.from_user.id in activate_bot:
            await state.set_state(gototwo.gotwo)
            await message.answer('По моему мы где-то виделись..', reply_markup=kb.go)
        else:
            await message.answer(F'Тут запуск с параметром, пока только это тестим. Параметр - {command.args}')
            await message.answer_photo(photo='AgACAgIAAxkBAAMbZx6IlcpY7w30CNaCgpMdRH5J_IgAAj3oMRtSUfBI700BRd9a40EBAAMCAAN5AAM2BA', caption='непонятная фотка и цепляющий текст, но который не понять без продолжения', reply_markup=kb.mesF, one_time_keyboard=True)
            if command.args == 'prodlink':
                await message.answer('Ну тут все четко, зашел по ссылке с квери "продлинк"')
            else:
                await message.answer('А тут ты по другому квери зашел')
    


@oneStage.message(CommandStart())
async def start(message: Message, state: FSMContext):
    await rq.setUser(tg_id=message.from_user.id, 
                     username=message.from_user.first_name)
    async with async_session() as session:
        # Выполнение запроса для получения всех ID пользователей
        result = await session.execute(select(UserPayment.tg_id))
        ids = result.scalars().all()
        global user_id
        user_id = message.from_user.id
        
        if message.from_user.id in ids:
            await message.answer('Кажется мы уже знакомы...', reply_markup=lkb.lesz)
        elif message.from_user.id in activate_bot:
            await state.set_state(gototwo.gotwo)
            await message.answer('По моему мы где-то виделись..', reply_markup=kb.go)
        else:
            await message.answer_photo(photo='AgACAgIAAxkBAAMbZx6IlcpY7w30CNaCgpMdRH5J_IgAAj3oMRtSUfBI700BRd9a40EBAAMCAAN5AAM2BA', caption='непонятная фотка и цепляющий текст, но который не понять без продолжения', reply_markup=kb.mesF, one_time_keyboard=True)


@oneStage.callback_query(F.data == 'otv')
async def mes1(callback: CallbackQuery):
    message = callback.message
    await message.edit_reply_markup()
    await message.answer_photo(photo='AgACAgIAAxkBAAMbZx6IlcpY7w30CNaCgpMdRH5J_IgAAj3oMRtSUfBI700BRd9a40EBAAMCAAN5AAM2BA', caption='другая по смыслу картинка, а текст начинает проясняться с дополнением', reply_markup=kb.mes1)


@oneStage.callback_query(F.data == 'otv1')
async def mes2(callback: CallbackQuery):
    message = callback.message
    await message.edit_reply_markup()
    await message.answer_photo(photo='AgACAgIAAxkBAAMbZx6IlcpY7w30CNaCgpMdRH5J_IgAAj3oMRtSUfBI700BRd9a40EBAAMCAAN5AAM2BA', caption='продолжение истории, все в шоках', reply_markup=kb.mes2)


@oneStage.callback_query(F.data == 'otv2')
async def mes3(callback: CallbackQuery):
    message = callback.message
    await message.edit_reply_markup()
    await message.answer_photo(photo='AgACAgIAAxkBAAMbZx6IlcpY7w30CNaCgpMdRH5J_IgAAj3oMRtSUfBI700BRd9a40EBAAMCAAN5AAM2BA', caption='потихоньку рассказываем о нас', reply_markup=kb.mes3)


@oneStage.callback_query(F.data == 'otv3')
async def mes4(callback: CallbackQuery, state: FSMContext):
    await state.set_state(gototwo.gotwo)
    message = callback.message    
    activate_bot.append(user_id)
    await message.edit_reply_markup()
    await message.answer_photo(photo='AgACAgIAAxkBAAMbZx6IlcpY7w30CNaCgpMdRH5J_IgAAj3oMRtSUfBI700BRd9a40EBAAMCAAN5AAM2BA', caption='воооот, переходим к основному, попадаем в главное меню!! \n\nпосле нажатия кнопки, соответственно', reply_markup=kb.go)


#"отв3" переводит нас дальше в файл тво.пу, там первый обработчик ловит "отв3" и происходит перевод в главное меню.
#Часть кода после комментария убрать!!! Это тестовая часть для проверки работоспособности!!!


@oneStage.message(Command('showidpayment'))
async def show_id(message: Message):
    async with async_session() as session:
        # Выполнение запроса для получения всех ID пользователей
        result = await session.execute(select(UserPayment.tg_id))
        ids = result.scalars().all()
        
        if ids:
            # Формирование строки с ID пользователей
            ids_text = '\n'.join(str(user_id) for user_id in ids)
            await message.reply(f"Список ID пользователей, которые купили:\n{ids_text}")
        else:
            await message.reply("В базе данных нет пользователей.")


@oneStage.message(Command('showid'))
async def show_id(message: Message):
    async with async_session() as session:
        # Выполнение запроса для получения всех ID пользователей
        result = await session.execute(select(User.tg_id))
        ids = result.scalars().all()
        
        if ids:
            # Формирование строки с ID пользователей
            ids_text = '\n'.join(str(user_id) for user_id in ids)
            await message.reply(f"Список ID пользователей:\n{ids_text}")
        else:
            await message.reply("В базе данных нет пользователей.")


@oneStage.message(F.photo)
async def GetPhotoID(message: Message):
    await message.answer(F'Вот айди фотки: {message.photo[-1].file_id}')