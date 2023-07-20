from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup

from aiogram import types


async def mi_line_btn():
    btn=types.InlineKeyboardMarkup(row_width=1)
    btn.add(
        types.InlineKeyboardButton("Купить ОСАГО",callback_data="n1"),
        types.InlineKeyboardButton("Техосмотр",callback_data="n2"),
        types.InlineKeyboardButton("Фотошоп техосмотр",callback_data="n3"),
        types.InlineKeyboardButton("КАСКО для банка",callback_data="n4"),
        types.InlineKeyboardButton("Карта учета ГИБДД",callback_data="n5"),
        types.InlineKeyboardButton("Карта ВУ по базе ГАИ",callback_data="n6"),
        types.InlineKeyboardButton("Поиск по базе Солярис",callback_data="n7"),
        types.InlineKeyboardButton("Для востоновленияКБМ",callback_data="n8"),
        types.InlineKeyboardButton("Договор купил продажи",callback_data="n9"),
        types.InlineKeyboardButton("Снятие ТС с учета",callback_data="n10"),
    )
    return btn

async def mi_liner_btn():
    btn=types.InlineKeyboardMarkup(row_width=1)
    btn.add(
        types.InlineKeyboardButton("Подробный прогноз",callback_data="n1"),
        types.InlineKeyboardButton("Пожертвование боту",callback_data="n2"),
    )
    return btn

async def mi_linere_btn():
    btn=types.InlineKeyboardMarkup(row_width=1)
    btn.add(
        types.InlineKeyboardButton("Пожертвование боту",callback_data="n1"),
    )
    return btn

async def mi_linerer_btn():
    btn=types.InlineKeyboardMarkup(row_width=2)
    btn.add(
        types.InlineKeyboardButton("Прогнозы на сегодня",callback_data="n1"),
        types.InlineKeyboardButton("Прогнозы на завтра",callback_data="n2"),
        types.InlineKeyboardButton("На 5 дней",callback_data="n3"),
        types.InlineKeyboardButton("На 10 дней",callback_data="n4"),
    )
    return btn