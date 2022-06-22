from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

b1= KeyboardButton('/start')
b2= KeyboardButton('/schedule')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client.add(b1).row(b2)

i1= InlineKeyboardButton(text='Вступительная компания', callback_data='vstup')
i2= InlineKeyboardButton(text='Факультети університету', callback_data='faculty')
i3= InlineKeyboardButton(text='Корпуси', callback_data='buildings')
i4= InlineKeyboardButton(text='ОНУ сад', callback_data='garden')
i5= InlineKeyboardButton(text='Приймальна комісія', callback_data='comission')
i6= InlineKeyboardButton(text='Гуртожиток', callback_data='living')
i7= InlineKeyboardButton(text='Корисні матеріали', callback_data='interesting')

inline1_c = InlineKeyboardMarkup(1)
inline1_c.add(i1, i2, i3, i4, i5, i6, i7)

fac1 = InlineKeyboardButton(text='Біофак',callback_data='bio')
fac2 = InlineKeyboardButton(text='Геолого-географічний факультет (ГГФ)',callback_data='ggf')
fac3 = InlineKeyboardButton(text='Економіко-правовий факультет (ЕПФ)',callback_data='epf')
fac4 = InlineKeyboardButton(text='Факультет історії та філософії (ФIФ)',callback_data='fif')
fac5 = InlineKeyboardButton(text='Факультет журналістики, реклами та видавничої справи (ФЖРВС)',callback_data='firbc')
fac6 = InlineKeyboardButton(text='Факультет математики, фізики та інформаційних технологій (ФМФIТ)',callback_data='fmfit')
fac7 = InlineKeyboardButton(text='Факультет міжнародних відносин, політології та соціології (ФМВПС)',callback_data='fmbpc')
fac8 = InlineKeyboardButton(text='Факультет психології та соціальної роботи (ФПСР)',callback_data='fpsr')
fac9 = InlineKeyboardButton(text='Факультет романо-германської філології (ФРГФ)',callback_data='rgf')
fac10 = InlineKeyboardButton(text='Філологічний факультет (Філфак)',callback_data='filfak')
fac11 = InlineKeyboardButton(text='Факультет хімїї та фармації (ФХФ)',callback_data='fxf')
fac12 = InlineKeyboardButton(text='Фаховий коледж',callback_data='college')
fac_back = InlineKeyboardButton(text='Назад', callback_data='fac_back')

fac_inline = InlineKeyboardMarkup(1).add(fac1,fac2,fac3,fac4,fac5,fac6,fac7,fac8,fac9,fac10,fac11,fac12,fac_back)

bio103= InlineKeyboardButton(text='Науки про Землю. Морська геологія, гідрогеологія та інженерна геологія', callback_data='103')
bio106= InlineKeyboardButton(text='Географічні основи менеджменту природокористування та регіонального і муніципального розвитку', callback_data='106')
bio242= InlineKeyboardButton(text='Туризм', callback_data='242')
bio014_17= InlineKeyboardButton(text='Середня освіта (Географія)', callback_data='014')
back_bio = InlineKeyboardButton(text='Назад',callback_data='back_bio')
bio_inline = InlineKeyboardMarkup(1).add(bio242,bio106,bio103,bio014_17,back_bio)



eco051=InlineKeyboardButton(text='Економіка. Економіка та правове регулювання бізнесу',callback_data='051')
eco071=InlineKeyboardButton(text='Облік і оподаткування',callback_data='071')
eco072=InlineKeyboardButton(text='Фінанси, банківська справа та страхування',callback_data='072')
eco073=InlineKeyboardButton(text='Менеджмент',callback_data='073')
eco081=InlineKeyboardButton(text='Право',callback_data='081')
back_eco = InlineKeyboardButton(text='Назад',callback_data='back_eco')
eco_inline = InlineKeyboardMarkup(1).add(eco081,eco073,eco072,eco071,eco051,back_eco)



hist032=InlineKeyboardButton(text='Історія та археологія',callback_data='032')
hist033=InlineKeyboardButton(text='Філософія',callback_data='033')
hist034=InlineKeyboardButton(text='Культурологія',callback_data='034')
back_hist = InlineKeyboardButton(text='Назад',callback_data='back_hist')
hist_inline = InlineKeyboardMarkup(1).add(hist034,hist033,hist032,back_hist)




journal061=InlineKeyboardButton('Журналістика',callback_data='061')
back_journal = InlineKeyboardButton(text='Назад',callback_data='back_journal')
journal_inline = InlineKeyboardMarkup(1).add(journal061,back_journal)


fmfit104= InlineKeyboardButton('Фізика та астрономія',callback_data='104')
fmfit105= InlineKeyboardButton('Прикладна фізика та наноматеріали',callback_data='105')
fmfit111= InlineKeyboardButton('Математика',callback_data='111')
fmfit113= InlineKeyboardButton('Прикладна математика',callback_data='113')
fmfit122= InlineKeyboardButton('Комп’ютерні науки',callback_data='122')
fmfit123= InlineKeyboardButton('Комп’ютерна інженерія',callback_data='123')
fmfit126= InlineKeyboardButton('Інформаційні системи та технології',callback_data='126')
fmfit151= InlineKeyboardButton('Автоматизація та комп’ютерно-інтегровані технології. Комп\'ютерна обробка та аналіз даних',callback_data='151')
fmfit014_08= InlineKeyboardButton('Середня освіта (Фізика)',callback_data='01408')
back_fmfit = InlineKeyboardButton(text='Назад',callback_data='back_fmfit')
fmfit_inline = InlineKeyboardMarkup(1).add(fmfit111,fmfit151,fmfit126,fmfit123,fmfit014_08,fmfit122,fmfit113,fmfit105,fmfit104,fmfit151,fmfit126,fmfit123,fmfit014_08,fmfit122,fmfit113,fmfit105,fmfit104,back_fmfit)


inter052=InlineKeyboardButton('Політологія',callback_data='052')
inter054=InlineKeyboardButton('Соціологія',callback_data='054')
inter291=InlineKeyboardButton('Міжнародні відносини, суспільні комунікації та регіональні студії',callback_data='291')
inter292=InlineKeyboardButton('Міжнародні економічні відносини',callback_data='292')
back_inter = InlineKeyboardButton(text='Назад',callback_data='back_inter')
inter_inline = InlineKeyboardMarkup(1).add(inter292,inter054,inter291,inter052,back_inter)


psycho053=InlineKeyboardButton('Психологія',callback_data='053')
psycho231=InlineKeyboardButton('Соціальна робота',callback_data='231')
back_psycho = InlineKeyboardButton(text='Назад',callback_data='back_psycho')
psycho_inline = InlineKeyboardMarkup(1).add(psycho231,psycho053,back_psycho)



rgf035_041=InlineKeyboardButton('Філологія. перша - англійська',callback_data='035_041')
rgf035_043=InlineKeyboardButton('Філологія. перша - німецька',callback_data='035_043')
rgf035_051=InlineKeyboardButton('Філологія. перша - іспанська',callback_data='035_051')
rgf035_055=InlineKeyboardButton('Філологія. перша - французька',callback_data='035_055')
back_rgf=InlineKeyboardButton('Назад',callback_data='back_rgf')
rgf_inline = InlineKeyboardMarkup(1).add(rgf035_055,rgf035_051,rgf035_043,rgf035_041,back_rgf)

filo035_01=InlineKeyboardButton('Філологія. Українська мова та література', callback_data='035_01')
filo035_10=InlineKeyboardButton('Прикладна лінгвістика',callback_data='035_10')
filo035_034=InlineKeyboardButton('Філологія. перша - російська',callback_data='035_034')
back_filo= InlineKeyboardButton('Назад',callback_data='back_filo')
filo_inline = InlineKeyboardMarkup(1).add(filo035_10,filo035_034,filo035_01,back_filo)

chemistry102=InlineKeyboardButton('Хімія',callback_data='102')
chemistry1022=InlineKeyboardButton('Фармацевтична хімія',callback_data='1022')
chemistry226=InlineKeyboardButton('Фармація, промислова фармація. Фармація',callback_data='226')
chemistry014_06=InlineKeyboardButton('Середня освіта (Хімія)',callback_data='014_06')
back_chem= InlineKeyboardButton('Назад', callback_data='back_chem')
chemistry_inline = InlineKeyboardMarkup(1).add(chemistry226,chemistry1022,chemistry102,chemistry014_06,back_chem)

college07=InlineKeyboardButton('Управління та адміністрування. Облік і оподаткування', callback_data='07')
college072=InlineKeyboardButton('Управління та адміністрування. Фінанси, банківська справа та страхування', callback_data='072')
college11=InlineKeyboardButton('Математика та статистика. Прикладна математика', callback_data='11')
college23=InlineKeyboardButton('Соціальна робота', callback_data='23')
back_college = InlineKeyboardButton('Назад',callback_data='back_college')
college_inline = InlineKeyboardMarkup(1).add(college07,college23,college11,college072,back_college)


int1 = InlineKeyboardButton(text='Відкриття Віртуальної навчальної фабрики в рамках Erasmus+', callback_data='first')
int2 = InlineKeyboardButton(text='Odesa I.I.Mechnikov National University: TRADITION & RECOGNITION', callback_data='second')
back_int = InlineKeyboardButton(text='Назад',callback_data='back_int')
interesting_inline = InlineKeyboardMarkup(1)
interesting_inline.add(int2,int1,back_int)


