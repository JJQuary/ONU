from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from create_bot import dp
from data_base import sqlite_db
from aiogram.dispatcher.filters import Text

from data_base.sqlite_db import sql_add_command

ID = 319637773

# class FSMAdmin(StatesGroup):
#     photo = State()
#     name = State()
#     description = State()
#     price = State()


# async def cm_start(message: types.Message):
#     if message.from_user.id == ID:
#         await message.reply('Загрузи фотку')
#         await FSMAdmin.photo.set()


# async def cancel_handler(message: types.Message, state: FSMContext):
#     current_state = await state.get_state()
#     if current_state is None:
#         return
#     await state.finish()
#     await message.reply('OK')


# async def load_photo(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['photo'] = message.photo[0].file_id
#     await FSMAdmin.next()
#     await message.reply("Теперь введи название")


# async def load_name(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['name'] = message.text
#
#     async with state.proxy() as data:
#         await sql_add_command(state)
#     await state.finish()


# def register_handlers_admin(dp: Dispatcher):
#     dp.register_message_handler(cm_start, commands='Post', state=None)
#     dp.register_message_handler(cancel_handler, state="*", commands='cancel')
#     dp.register_message_handler(cancel_handler, Text(equals='cancel', ignore_case=True), state="*")
#     dp.register_message_handler(load_photo, content_types=['photo'], state=FSMAdmin.photo)
#     dp.register_message_handler(load_name, state=FSMAdmin.name)

