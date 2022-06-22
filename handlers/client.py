from aiogram import types, Dispatcher
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from data_base.sqlite_db import sql_add_command

from create_bot import bot
from keyboards import client_kb

class FSMClient(StatesGroup):
    lvl1 = State()
    lvl2 = State()

ID = 319637773


async def command_start(message: types.Message):
        await bot.send_message(message.from_user.id, 'Здравствуйте ', reply_markup=client_kb.inline1_c)
        await message.delete()


async def work_graph(message: types.Message):
    await bot.send_message(message.from_user.id, 'Выберите нужный вам вариант')
    await message.delete()


# async def ONU_place_command(message: types.Message):
#     await bot.send_message(message.from_user.id, 'ул. Мечникова 15', reply_markup=ReplyKeyboardRemove())
#     await message.delete()

# async def cm_start(message: types.Message):
#     await FSMClient.lvl1.set()
#     await message.answer('Choose',reply_markup=client_kb.inline1_c)

# async def cancel_handler(message: types.Message, state: FSMContext):
#     current_state = await state.get_state()
#     if current_state is None:
#         return
#     await state.finish()
#     await message.reply('OK',reply_markup=client_kb.kb_client)

# async def load_photo(message: types.Message,state :FSMContext):
#     message.text.lower()
#     if message.text == 'Вступительная компания':
#         async with state.proxy() as data:
#             data['lvl1'] = message.text
#         await message.answer_document( open(r'C:/Users/JJQuary/PycharmProjects/AiogramBot/files/pravila.pdf', 'rb'), reply_markup=cancel)
#             # await bot.send_document(message.from_user.id, open(r'C:/Users/JJQuary/PycharmProjects/AiogramBot/files/pravila.pdf', 'rb'))
#     if message.text == 'Факультети університету':
#         async with state.proxy() as data:
#             data['lvl1'] = message.text
#
#     if message.text == 'Корпуси':
#         async with state.proxy() as data:
#             data['lvl1'] = message.text
#         await message.reply('https://www.youtube.com/watch?v=lqg9eIQJph8&t=13s', reply_markup=cancel)
#     if message.text == 'ОНУ сад':
#         async with state.proxy() as data:
#             data['lvl1'] = message.text
#         await message.reply('https://www.youtube.com/watch?v=PVJYorsiMts', reply_markup=cancel)
#     if message.text == 'Приймальна комісія':
#         async with state.proxy() as data:
#             data['lvl1'] = message.text
#         await message.reply('Приймальна комісія: Французький бульвар 24/26 '
#                           'т (+380482) 68-12-84;  (+38-0482) 68-18-58'
#                           'vstup@onu.edu.ua    http://vstup.onu.edu.ua/', reply_markup=cancel)
#     if message.text == 'Гуртожиток':
#         async with state.proxy() as data:
#             data['lvl1'] = message.text


async def first_c(call: types.CallbackQuery):
    if call.data == 'vstup':
        await call.message.edit_text('http://vstup.onu.edu.ua/storage/files/vstupna_kompaniya/pravyla_priomu/pravila_pryomu_ONU_2022.pdf',
                                      reply_markup=client_kb.inline1_c)
    elif call.data == 'faculty':
        await call.message.edit_text('Наявні факультети',reply_markup=client_kb.fac_inline)
    elif call.data == 'bio':
        await call.message.edit_text('Наявні спеціальності',reply_markup=client_kb.bio_inline)
    elif call.data == '106':
        await call.message.edit_text('1', reply_markup=client_kb.bio_inline)
    elif call.data == '242':
        await call.message.edit_text('2', reply_markup=client_kb.bio_inline)
    elif call.data == '014':
        await call.message.edit_text('3', reply_markup=client_kb.bio_inline)
    elif call.data == 'back_bio':
        await call.message.edit_text('Наявні спеціальності',reply_markup= client_kb.fac_inline)
    elif call.data == '051':
        await call.message.edit_text('3',reply_markup=client_kb.eco_inline)
    elif call.data == '071':
        await call.message.edit_text('4',reply_markup=client_kb.eco_inline)
    elif call.data == '072':
        await call.message.edit_text('5',reply_markup=client_kb.eco_inline)
    elif call.data == '073':
        await call.message.edit_text('6',reply_markup=client_kb.eco_inline)
    elif call.data == '081':
        await call.message.edit_text('7',reply_markup=client_kb.eco_inline)
    elif call.data == 'back_eco':
        await call.message.edit_text('Наявні спеціальності',reply_markup= client_kb.fac_inline)
    elif call.data == '032':
        await call.message.edit_text('8',reply_markup=client_kb.hist_inline)
    elif call.data == '033':
        await call.message.edit_text('9',reply_markup=client_kb.hist_inline)
    elif call.data == '034':
        await call.message.edit_text('10',reply_markup=client_kb.hist_inline)
    elif call.data == 'back_hist':
        await call.message.edit_text('Наявні спеціальності',reply_markup= client_kb.fac_inline )
    elif call.data == '061':
        await call.message.edit_text('11',reply_markup=client_kb.journal_inline)
    elif call.data == 'back_journal':
        await call.message.edit_text('Наявні спеціальності',reply_markup= client_kb.fac_inline)
    elif call.data == '104':
        await call.message.edit_text('12',reply_markup=client_kb.fmfit_inline)
    elif call.data == '105':
        await call.message.edit_text('13',reply_markup=client_kb.fmfit_inline)
    elif call.data == '111':
        await call.message.edit_text('14',reply_markup=client_kb.fmfit_inline)
    elif call.data == '113':
        await call.message.edit_text('15',reply_markup=client_kb.fmfit_inline)
    elif call.data == '122':
        await call.message.edit_text('16',reply_markup=client_kb.fmfit_inline)
    elif call.data == '123':
        await call.message.edit_text('17',reply_markup=client_kb.fmfit_inline)
    elif call.data == '126':
        await call.message.edit_text('18',reply_markup=client_kb.fmfit_inline)
    elif call.data == '151':
        await call.message.edit_text('19',reply_markup=client_kb.fmfit_inline)
    elif call.data == '01408':
        await call.message.edit_text('20',reply_markup=client_kb.fmfit_inline)
    elif call.data == 'back_fmfit':
        await call.message.edit_text('Наявні спеціальності',reply_markup= client_kb.fac_inline)
    elif call.data == '052':
        await call.message.edit_text('21',reply_markup=client_kb.inter_inline)
    elif call.data == '054':
        await call.message.edit_text('22',reply_markup=client_kb.inter_inline)
    elif call.data == '291':
        await call.message.edit_text('23',reply_markup=client_kb.inter_inline)
    elif call.data == '292':
        await call.message.edit_text('24',reply_markup=client_kb.inter_inline)
    elif call.data == 'back_inter':
        await call.message.edit_text('Наявні спеціальності',reply_markup= client_kb.fac_inline)
    elif call.data == '053':
        await call.message.edit_text('25',reply_markup=client_kb.psycho_inline)
    elif call.data == '231':
        await call.message.edit_text('26',reply_markup=client_kb.psycho_inline)
    elif call.data == 'back_psycho':
        await call.message.edit_text('Наявні спеціальності',reply_markup= client_kb.fac_inline)
    elif call.data == '035_041':
        await call.message.edit_text('27',reply_markup=client_kb.rgf_inline)
    elif call.data == '035_043':
        await call.message.edit_text('28',reply_markup=client_kb.rgf_inline)
    elif call.data == '035_051':
        await call.message.edit_text('29',reply_markup=client_kb.rgf_inline)
    elif call.data == '035_055':
        await call.message.edit_text('30',reply_markup=client_kb.rgf_inline)
    elif call.data == 'back_rgf':
        await call.message.edit_text('Наявні спеціальності',reply_markup= client_kb.fac_inline)
    elif call.data == '035_01':
        await call.message.edit_text('31',reply_markup=client_kb.filo_inline)
    elif call.data == '035_10':
        await call.message.edit_text('32',reply_markup=client_kb.filo_inline)
    elif call.data == '035_034':
        await call.message.edit_text('33',reply_markup=client_kb.filo_inline)
    elif call.data == 'back_filo':
        await call.message.edit_text('Наявні спеціальності',reply_markup= client_kb.fac_inline)
    elif call.data == '102':
        await call.message.edit_text('34',reply_markup=client_kb.chemistry_inline)
    elif call.data == '1022':
        await call.message.edit_text('35',reply_markup=client_kb.chemistry_inline)
    elif call.data == '226':
        await call.message.edit_text('36',reply_markup=client_kb.chemistry_inline)
    elif call.data == '014_06':
        await call.message.edit_text('37',reply_markup=client_kb.chemistry_inline)
    elif call.data == 'back_chem':
        await call.message.edit_text('Наявні спеціальності',reply_markup=client_kb.fac_inline)
    elif call.data == '07':
        await call.message.edit_text('38',reply_markup=client_kb.college_inline)
    elif call.data == '072':
        await call.message.edit_text('39',reply_markup=client_kb.college_inline)
    elif call.data == '11':
        await call.message.edit_text('40',reply_markup=client_kb.college_inline)
    elif call.data == '23':
        await call.message.edit_text('41',reply_markup=client_kb.college_inline)
    elif call.data == 'back_college':
        await call.message.edit_text('Наявні спеціальності',reply_markup=client_kb.fac_inline)
    elif call.data == 'ggf':
        await call.message.edit_text('Наявні спеціальності',reply_markup=client_kb.bio_inline)
    elif call.data == 'epf':
        await call.message.edit_text('Наявні спеціальності',reply_markup=client_kb.eco_inline)
    elif call.data == 'fif':
        await call.message.edit_text('Наявні спеціальності',reply_markup=client_kb.hist_inline)
    elif call.data == 'firbc':
        await call.message.edit_text('Наявні спеціальності',reply_markup=client_kb.journal_inline)
    elif call.data == 'fmfit':
        await call.message.edit_text('Наявні спеціальності',reply_markup=client_kb.fmfit_inline)
    elif call.data == 'fmbpc':
        await call.message.edit_text('Наявні спеціальності',reply_markup=client_kb.inter_inline)
    elif call.data == 'fpsr':
        await call.message.edit_text('Наявні спеціальності',reply_markup=client_kb.psycho_inline)
    elif call.data == 'filfak':
        await call.message.edit_text('Наявні спеціальності',reply_markup=client_kb.filo_inline)
    elif call.data == 'fxf':
        await call.message.edit_text('Наявні спеціальності',reply_markup=client_kb.chemistry_inline)
    elif call.data == 'college':
        await call.message.edit_text('ІСТОРІЯ ЗАСНУВАННЯ КОЛЕДЖУ'
                                     ' У 1996 році Одеський національний університет імені І.І.Мечникова на виконання Закону України «Про освіту», постанови Кабінету Міністрів України «Про затвердження Положення про освітньо-кваліфікаційні рівні (ступеневу освіту)» ініціював перед Міністерством освіти і науки України створення інноваційної моделі триступневої вищої освіти. '
                                     'З метою реалізації цієї системи в університеті був створений Коледж підприємництва та соціальної роботи (наказ Міністра освіти від 18.06.1998р. №224). У 1999 році (наказ Міністра освіти і науки України №14 від 14.01.1999р.) Коледж став базовим для створення експериментальних майданчиків «Школа-Коледж-Університет» при ОНУ імені І.І.Мечникова. '
                                     'З метою приведення до вимог чинного законодавства назви структурного підрозділу університету з 2012 року Коледж перейменовано у Коледж економіки та соціальної роботи (наказ Міністра освіти і науки, молоді та спорту від 06.11.2012р. №1247), а з 2020 року - Фаховий коледж ОНУ імені І.І. Мечникова'
                                     ,reply_markup=client_kb.college_inline)
    elif call.data == 'fac_back':
        await call.message.edit_text('Выберите нужный вариант',reply_markup=client_kb.inline1_c)
    elif call.data == 'buildings':
        await call.message.edit_text('https://www.youtube.com/watch?v=lqg9eIQJph8&t=13s',reply_markup=client_kb.inline1_c)
    elif call.data == 'garden':
        await call.message.edit_text('https://www.youtube.com/watch?v=PVJYorsiMts',reply_markup=client_kb.inline1_c)
    elif call.data == 'comission':
        await call.message.edit_text('Приймальна комісія: Французький бульвар 24/26 '
                                  'т (+380482) 68-12-84;  (+38-0482) 68-18-58'
                                  'vstup@onu.edu.ua    http://vstup.onu.edu.ua/', reply_markup=client_kb.inline1_c)
    elif call.data == 'living' :
        await call.message.edit_text('http://vstup.onu.edu.ua/pro-universytet/hurtozhytky',reply_markup=client_kb.inline1_c)
    elif call.data == 'interesting':
        await call.message.edit_text('Корисні матеріали',reply_markup=client_kb.interesting_inline)
    elif call.data == 'first':
        await call.message.edit_text('https://www.youtube.com/watch?v=ltIQU5iNdkg', reply_markup=client_kb.interesting_inline)
    elif call.data == 'second':
        await call.message.edit_text('https://www.youtube.com/watch?v=AMqnYdGPuvc', reply_markup=client_kb.interesting_inline)
    elif call.data == 'back_int':
        await call.message.edit_text('Выберите нужный вам вариант',reply_markup=client_kb.inline1_c)

# async def load_photo(call: types.CallbackQuery, state: FSMContext):
#     async with state.proxy() as data:
#         data['lvl1'] = call.data
    # if call.data == 'faculty':
    #     await bot.send_message(call.from_user.id, 'fwafs')
    #     await FSMClient.lvl1.set()
    # elif call.data == 'vstup':
    #     await call.answer("Выбери факультет", reply_markup=ReplyKeyboardRemove)
    #     # await bot.send_document(call.id, open('../files/pravila.pdf'))
    #     await FSMClient.lvl1.set()
    # elif call.data == 'buildings':
    #     await call.answer("Выбери факультет", reply_markup=ReplyKeyboardRemove)
    #     await FSMClient.lvl1.set()
    # elif call.data == 'garden':
    #     await call.answer("Выбери факультет", reply_markup=ReplyKeyboardRemove)
    #     await FSMClient.lvl1.set()
    # elif call.data == 'comission':
    #     await call.answer("Приймальна комісія: Французький бульвар 24/26, ", reply_markup=ReplyKeyboardRemove)
    #     await FSMContext.finish()
    # elif call.data == 'living':
    #     await call.answer("Выбери факультет", reply_markup=ReplyKeyboardRemove)
    #     await FSMClient.lvl1.set()
    # elif call.data == 'interesting':
    #     await call.answer("Выбери факультет", reply_markup=ReplyKeyboardRemove)
    #     await FSMClient.lvl1.set()
    # else: await bot.send_message(call.from_user.id, 'fawfafaw')


# async def load_name(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['lvl2'] = message.text
#
#     async with state.proxy() as data:
#         await sql_add_command(state)
#     await state.finish()

# async def menu(call: types.CallbackQuery):
#     await bot.answer_callback_query(call.id)
#     if call.data == 'vstup':
#         await bot.send_message(call.from_user.id,'Первый пункт',reply_markup=client_kb.inline1_c)
#     elif call.data == 'lvl1':
#         await bot.send_message(call.from_user.id,'2 пункт',reply_markup=ReplyKeyboardRemove())
#     elif call.data == 'college':
#         await bot.send_message(call.from_user.id,'3 пункт',reply_markup=ReplyKeyboardRemove())


def register_handlers_client(dp: Dispatcher):

    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_callback_query_handler(first_c)
    # dp.register_message_handler(cm_start, commands='schedule', state=None)
    # dp.register_message_handler(ONU_place_command, commands=['contacts'])
    # dp.register_message_handler(cancel_handler, state="*", commands='cancel')
    # dp.register_message_handler(cancel_handler, Text(equals='Отмена', ignore_case=True), state="*")
    # dp.register_message_handler(load_photo, state=FSMClient.lvl1)
    # dp.register_message_handler(load_name, state=FSMClient.lvl2)
