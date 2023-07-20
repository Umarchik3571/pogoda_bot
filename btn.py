
bosh_menuu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🌎 Изменить город"),
        ],   
        [
            KeyboardButton(text="📏 Единицы измерения"),
            KeyboardButton(text="🇷🇺/🇬🇧 Язык"),
        ],
        [
            KeyboardButton(text="⚙️ Настройки"),
        ],
        [
            KeyboardButton(text="↩️ Назад"),
        ],
    ],
    resize_keyboard=True
)