from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

bot = Bot('5153493879:AAGMZ5B7rrdO78aj-Gxydf-Yih_iDtcrBmo')
dp = Dispatcher(bot, storage=storage)