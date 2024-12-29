from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

threeStage = Router()
import keyboard.keyThree as lkb


@threeStage.callback_query(F.data == 'lesson1')
async def mes1(callback: CallbackQuery):
    message = callback.message
    await message.edit_reply_markup()
    await message.edit_text('Вот первый урок, тратататататтатататататататтатат. Теперь ты автомат. \n\n\nДальше короче надо распихать материал, сделать возможность листать дни.'
                         ' Сейчас осталось только впихнуть материал и деплоить на сервер', reply_markup=lkb.les2)


@threeStage.callback_query(F.data == 'lesson2')
async def mes2(callback: CallbackQuery):
    message = callback.message
    await message.edit_text('урок 2', reply_markup=lkb.les3)


@threeStage.callback_query(F.data == 'lesson3')
async def mes2(callback: CallbackQuery):
    message = callback.message
    await message.edit_text('урок 3', reply_markup=lkb.les4)


@threeStage.callback_query(F.data == 'lesson4')
async def mes2(callback: CallbackQuery):
    message = callback.message
    await message.edit_text('урок 4', reply_markup=lkb.les5)


@threeStage.callback_query(F.data == 'lesson5')
async def mes2(callback: CallbackQuery):
    message = callback.message
    await message.edit_text('урок 5', reply_markup=lkb.les6)


@threeStage.callback_query(F.data == 'lesson6')
async def mes2(callback: CallbackQuery):
    message = callback.message
    await message.edit_text('урок 6', reply_markup=lkb.les7)


@threeStage.callback_query(F.data == 'lesson7')
async def mes2(callback: CallbackQuery):
    message = callback.message
    await message.edit_text('урок 7', reply_markup=lkb.les8)


@threeStage.callback_query(F.data == 'lesson8')
async def mes2(callback: CallbackQuery):
    message = callback.message
    await message.edit_text('урок 8', reply_markup=lkb.les9)


@threeStage.callback_query(F.data == 'lesson9')
async def mes2(callback: CallbackQuery):
    message = callback.message
    await message.edit_text('урок 9', reply_markup=lkb.les10)


@threeStage.callback_query(F.data == 'lesson10')
async def mes2(callback: CallbackQuery):
    message = callback.message
    await message.edit_text('урок 10', reply_markup=lkb.les11)


@threeStage.callback_query(F.data == 'lesson11')
async def mes2(callback: CallbackQuery):
    message = callback.message
    await message.edit_text('урок 11', reply_markup=lkb.les12)


@threeStage.callback_query(F.data == 'lesson12')
async def mes2(callback: CallbackQuery):
    message = callback.message
    await message.edit_text('урок 12', reply_markup=lkb.les13)


@threeStage.callback_query(F.data == 'lesson13')
async def mes2(callback: CallbackQuery):
    message = callback.message
    await message.edit_text('урок 13', reply_markup=lkb.les14)


@threeStage.callback_query(F.data == 'lesson14')
async def mes2(callback: CallbackQuery):
    message = callback.message
    await message.edit_text('урок 14', reply_markup=lkb.les15)


@threeStage.callback_query(F.data == 'lesson15')
async def mes2(callback: CallbackQuery):
    message = callback.message
    await message.edit_text('урок 15', reply_markup=lkb.les16)


@threeStage.callback_query(F.data == 'lesson16')
async def mes2(callback: CallbackQuery):
    message = callback.message
    await message.edit_text('урок 16', reply_markup=lkb.les17)


@threeStage.callback_query(F.data == 'lesson17')
async def mes2(callback: CallbackQuery):
    message = callback.message
    await message.edit_text('урок 17', reply_markup=lkb.les18)


@threeStage.callback_query(F.data == 'lesson18')
async def mes2(callback: CallbackQuery):
    message = callback.message
    await message.edit_text('урок 18', reply_markup=lkb.les19)


@threeStage.callback_query(F.data == 'lesson19')
async def mes2(callback: CallbackQuery):
    message = callback.message
    await message.edit_text('урок 19', reply_markup=lkb.les20)


@threeStage.callback_query(F.data == 'lesson20')
async def mes2(callback: CallbackQuery):
    message = callback.message
    await message.edit_text('урок 20', reply_markup=lkb.les21)


@threeStage.callback_query(F.data == 'lesson21')
async def mes2(callback: CallbackQuery):
    message = callback.message
    await message.edit_text('урок 21', reply_markup=lkb.les22)


@threeStage.callback_query(F.data == 'lesson22')
async def mes2(callback: CallbackQuery):
    message = callback.message
    await message.edit_text('урок 22', reply_markup=lkb.les23)


@threeStage.callback_query(F.data == 'lesson23')
async def mes2(callback: CallbackQuery):
    message = callback.message
    await message.edit_text('урок 23', reply_markup=lkb.les24)


@threeStage.callback_query(F.data == 'lesson24')
async def mes2(callback: CallbackQuery):
    message = callback.message
    await message.edit_text('урок 24', reply_markup=lkb.les25)


@threeStage.callback_query(F.data == 'lesson25')
async def mes2(callback: CallbackQuery):
    message = callback.message
    await message.edit_text('урок 25', reply_markup=lkb.les26)


@threeStage.callback_query(F.data == 'lesson26')
async def mes2(callback: CallbackQuery):
    message = callback.message
    await message.edit_text('урок 26', reply_markup=lkb.les27)


@threeStage.callback_query(F.data == 'lesson27')
async def mes2(callback: CallbackQuery):
    message = callback.message
    await message.edit_text('урок 27', reply_markup=lkb.les28)


@threeStage.callback_query(F.data == 'lesson28')
async def mes2(callback: CallbackQuery):
    message = callback.message
    await message.edit_text('урок 28', reply_markup=lkb.les29)


@threeStage.callback_query(F.data == 'lesson29')
async def mes2(callback: CallbackQuery):
    message = callback.message
    await message.edit_text('урок 29', reply_markup=lkb.les30)


@threeStage.callback_query(F.data == 'lesson30')
async def mes2(callback: CallbackQuery):
    message = callback.message
    await message.edit_text('урок 30', reply_markup=lkb.les31)


@threeStage.callback_query(F.data == 'alllessons')
async def mes2(callback: CallbackQuery):
    message = callback.message
    await message.edit_text('Вот список всех уроков', reply_markup=lkb.lesmein)
