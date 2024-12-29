from database.models import async_session
from database.models import User, UserPayment
from sqlalchemy import select 


async def setUser(tg_id, username):
    async with async_session() as session:
        user = await session.scalar(select(User).filter_by(tg_id=tg_id))

        if not user:
            new_user = User(tg_id=tg_id, username=username)
            session.add(new_user)
            await session.commit()


async def setUserPayment(tg_id, username):
    async with async_session() as session:
        user = await session.scalar(select(UserPayment).filter_by(tg_id=tg_id))

        if not user:
            new_user_payment = UserPayment(tg_id=tg_id, username=username)
            session.add(new_user_payment)
            await session.commit()
