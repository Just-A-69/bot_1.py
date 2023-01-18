import telebot
import sys
from telebot import types

TOKEN = "Token"
bot = telebot.TeleBot(TOKEN)


def create_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    drink_btn = types.InlineKeyboardButton(text='Пить давай, да!?', callback_data='1')
    eat_btn = types.InlineKeyboardButton(text='Есть давай, да!?', callback_data='2')
    walk_btn = types.InlineKeyboardButton(text='Гулять давай, да!?', callback_data='3')
    sleep_btn = types.InlineKeyboardButton(text='Спать давай, да!?', callback_data='4')
    joke_btn = types.InlineKeyboardButton(text='шутку давай, да!?', callback_data='5')
    exit_btn = types.InlineKeyboardButton(text='Завершать давай, да!?', callback_data='6')
    keyboard.add(drink_btn, eat_btn, walk_btn, sleep_btn, joke_btn, exit_btn)
    return keyboard


@bot.message_handler(commands=['start', 'старт', 'гоушки'])
def start_bot(message):
    bot.send_message(message.chat.id, 'шалом, православый! Что хотиш?', reply_markup=create_keyboard())


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.message:
        if call.data == '1':
            img = open('water.jpg', 'rb')
            bot.send_photo(chat_id=call.message.chat.id,
                           photo=img,
                           caption='На, попей',
                           reply_markup=create_keyboard()
                           )
            img.close()

        if call.data == '2':
            img = open('food.jpg', 'rb')
            bot.send_photo(chat_id=call.message.chat.id,
                           photo=img,
                           caption='Братишка,я тебе покушать принес',
                           reply_markup=create_keyboard()
                           )
            img.close()

        if call.data == '3':
            bot.send_photo(chat_id=call.message.chat.id,
                           photo='https://upload.wikimedia.org/wikipedia/en/0/0a/Walk_%28song%29.jpg',
                           caption='https://youtu.be/AkFqg5wAuFk',
                           reply_markup=create_keyboard()
                           )

        if call.data == '4':
            bot.send_photo(chat_id=call.message.chat.id,
                           photo= 'https://www.ageuk.org.uk/globalassets/age-uk/media/hero/sleeping-cat-crop.jpg',
                           caption='Zzz...',
                           reply_markup=create_keyboard()
                           )

        if call.data == '5':
            bot.send_message(chat_id=call.message.chat.id,
                             text='https://baneks.ru/random',
                             disable_web_page_preview=True,
                             reply_markup=create_keyboard()
                             )

        if call.data == '6':
            bot.send_message(chat_id=call.message.chat.id,
                             text='Удачи тебе, сталкер!',
                             )
            sys.exit()


bot.infinity_polling()
