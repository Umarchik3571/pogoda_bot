import logging

from aiogram import Bot,Dispatcher, executor, types
from btn import bosh_menu, bosh_menuu
from inline_btn import mi_line_btn, mi_liner_btn,mi_linere_btn,mi_linerer_btn


BOT_TOKEN = '6081129928:AAHQ0UPgUEomNZHGc98ZLTqasG2OV7xDhtw'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN, parse_mode="html")
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.answer(text="Вот список того, что я умею:",reply_markup=bosh_menu)

@dp.message_handler(text='🌞 Погода сейчас')
async def send_welcomee(message: types.Message):
    img = types.InputFile("с.jpg")
    await message.answer_photo(photo=img,reply_markup= await mi_liner_btn())


@dp.message_handler(text='🔮 На 5 дней')
async def send_welcomee(message: types.Message):
    img = types.InputFile("p.jpg")
    await message.answer_photo(photo=img,reply_markup= await mi_linere_btn())
    
@dp.message_handler(text='🌅 На завтра')
async def send_welcomeee(message: types.Message):
    img = types.InputFile("o.jpg")
    await message.answer_photo(photo=img,reply_markup= await mi_linere_btn())

@dp.message_handler(text='🔮 На 10 дней')
async def send_welcomeeee(message: types.Message):
    img = types.InputFile("g.jpg")
    await message.answer_photo(photo=img,reply_markup= await mi_linere_btn())

@dp.message_handler(text='🔔 Уведомления')
async def send_welcomeeee(message: types.Message):
    await message.answer("Выберите тип отправляемых уведомлений:",reply_markup=await mi_linerer_btn())

@dp.message_handler(text='⚙️ Настройки')
async def send_welcomeeee(message: types.Message):
    await message.answer("⚙️ Настройки",reply_markup=bosh_menuu)

@dp.message_handler(text='↩️ Назад')
async def send_welcomeeee(message: types.Message):
    await message.answer("Вот список того, что я умею:",reply_markup=bosh_menu)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)