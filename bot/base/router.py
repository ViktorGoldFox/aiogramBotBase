from aiogram import types
from aiogram import Router
from aiogram.filters import Command

from logzero import logger
from sqlalchemy.ext.asyncio import AsyncSession

from database import db_helper
import bot.base.crud as crud
from untities import User

base_router = Router()

@base_router.message(Command("start"))
async def bot_start(message: types.Message):
    logger.debug(f"bot_start \n Username: {message.from_user.username} \n User_id: {message.from_user.id}")
    session: AsyncSession = db_helper.get_scoped_session()

    new_user: User = User(id=message.from_user.id, name=message.from_user.username)

    await crud.create_profile(session, new_user)

    await message.answer("Start")

    logger.info(f"@{message.from_user.username} вывел start")

    await session.close()

@base_router.message(Command("profile"))
async def bot_profile(message: types.Message):
    logger.debug(f"bot_profile \n Username: {message.from_user.username} \n User_id: {message.from_user.id}")
    session: AsyncSession = db_helper.get_scoped_session()

    user_data = await crud.get_profile(session, message.from_user.id)

    await message.answer(f"""
Id: {user_data.id}
Name: {user_data.name}
    """)

    logger.info(f"@{message.from_user.username} вывел profile")

    await session.close()

@base_router.message(Command("stop"))
async def bot_stop(message: types.Message):
    logger.debug(f"bot_stop \n Username: {message.from_user.username} \n User_id: {message.from_user.id}")
    session: AsyncSession = db_helper.get_scoped_session()

    await crud.del_profile(session, message.from_user.id)

    await message.answer("stop")

    logger.info(f"@{message.from_user.username} вывел stop")

    await session.close()