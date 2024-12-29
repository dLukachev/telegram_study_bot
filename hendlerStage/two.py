import asyncio
from aiogram import F, Router, Bot, types
from aiogram.types import CallbackQuery, PreCheckoutQuery, Message
import tracemalloc
from aiogram.types import LabeledPrice
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from Config import TOKEN, PROVTOKEN
import keyboard.keyTwo as kbt
import keyboard.keyOne as kb
import keyboard.keyThree as lkb
import database.requests as rq
from hendlerStage.one import gototwo

prices = [
    LabeledPrice(label='Название товара', amount=999 * 100)
]

twoStage = Router()
bot = Bot(token=TOKEN)

class pay(StatesGroup):
    done = State()


@twoStage.message(F.text == 'Звучит пока интересно..', gototwo.gotwo)
async def two(message: Message, state: FSMContext):
    global idUser
    idUser = message.from_user.id
    await state.clear()
    await message.answer('Содержание: тут короче очень важная информация, на такую то тему, вот столько человек интересовались ей за последнее время и вы тоже входите в этот процент\n\n\nТак вот'
                         'все, продолжаем! Тык по кнопке и появляется основная менюшка', reply_markup=kb.mes5)


@twoStage.callback_query(F.data == 'otv5')
async def mainmenumes(callback: CallbackQuery):
    message = callback.message
    await message.edit_text('Нам короче тоже кушать надо, программисту тоже кушать надо, они сначала назвали заоблочную цену, 4999'
                            'но я выбил специально для вас дешевле, за 999 отдам!!!!!!', reply_markup=kbt.mainMenu)


@twoStage.callback_query(F.data == 'info')
async def mainmenumes(callback: CallbackQuery):
    message = callback.message
    await message.edit_text('Здесь находится информация о курсе', reply_markup=kbt.infoCourse)


@twoStage.callback_query(F.data == 'infome')
async def mainmenumes(callback: CallbackQuery):
    message = callback.message
    await message.edit_text('Здесь находится выдуманная информация о боте, мол он не живой)))', reply_markup=kbt.infoCourse)


@twoStage.callback_query(F.data == 'otz')
async def mainmenumes(callback: CallbackQuery):
    message = callback.message
    await message.edit_text('Здесь находятся отзывы', reply_markup=kbt.moreOtz)


@twoStage.callback_query(F.data == 'day')
async def mainmenumes(callback: CallbackQuery):
    message = callback.message
    await message.edit_text('Здесь находится пример дня из курса', reply_markup=kbt.infoDay)


@twoStage.callback_query(F.data == 'program')
async def mainmenumes(callback: CallbackQuery):
    message = callback.message
    await message.edit_text('Здесь находится программа курса', reply_markup=kbt.infoProgram)


@twoStage.callback_query(F.data == 'moreOtz')
async def mainmenumes(callback: CallbackQuery):
    message = callback.message
    await message.edit_text('Здесь находятся ЕЩЕ отзывы', reply_markup=kbt.back)


@twoStage.callback_query(F.data == 'payment')
async def paymentymoney(callback: CallbackQuery):
    message = callback.message
    await asyncio.sleep(delay=1)
    tracemalloc.start()
    await bot.send_invoice(chat_id=idUser, 
                           payload='1', title='Оплата твоего лучшего обучения', 
                           description='Ну тут описание самое крутое!!!', 
                           provider_token=PROVTOKEN, 
                           currency='RUB', 
                           prices=prices)


@twoStage.pre_checkout_query(lambda query: True)
async def process_pre_checkout_query(pre_checkout_query: PreCheckoutQuery):
    await bot.answer_pre_checkout_query(
        pre_checkout_query.id,
        ok=True  # Можно добавить сообщение, если нужно
        # error_message='Ошибка при проведении платежа, попробуйте снова.'  # Используйте, если ok=False
    )


@twoStage.message(F.successful_payment)
async def handle_successful_payment(message: types.Message, state: FSMContext):
    successful_payment = message.successful_payment

    # Извлечение информации о платеже
    amount = successful_payment.total_amount / 99900  # Обычно сумма передается в копейках
    currency = successful_payment.currency
    invoice_payload = successful_payment.invoice_payload
    provider_payment_charge_id = successful_payment.provider_payment_charge_id
    telegram_payment_charge_id = successful_payment.telegram_payment_charge_id

    # Обработка информации о платеже (например, сохранение в базе данных)
    # Здесь вы можете добавить свой код для обработки платежа

    # Отправка подтверждения пользователю
    await message.answer(
        f"Спасибо за вашу оплату!\n"
        f"Выдаю все доступы!", reply_markup=kbt.go
    )
    await state.set_state(pay.done)
    await rq.setUserPayment(tg_id=idUser,
                            username=message.from_user.first_name)


@twoStage.message(F.text=='Давай учиться уже!', pay.done)
async def two(message: Message, state: FSMContext):
    await state.clear()
    await message.delete()
    await message.answer('Готово', reply_markup=lkb.les)
