
from email import message
from telebot import types
import telebot

bot = telebot.TeleBot('5404881483:AAE3KWWn5Cu_TDWTsQB2j2SllYEN1IrCL8w')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text='Наши соц.сети', callback_data='full_social_networks'))
    markup.add(types.InlineKeyboardButton(text='Информация', callback_data='information'))
    bot.send_message(message.chat.id, 'Что вы хотите узнать?', reply_markup=markup)
    

@bot.callback_query_handler(func=lambda call: True)
def socials(call):
    full_socials = types.InlineKeyboardMarkup()
    instagram = types.InlineKeyboardButton('Instagram', url='https://www.instagram.com/')
    youtube = types.InlineKeyboardButton('Youtube', url='https://youtube.com')
    tiktok = types.InlineKeyboardButton('TikTok', url='https://tiktok.com')
    full_socials.add(youtube,instagram, tiktok)
    if call.data == 'full_social_networks':
        text = 'Все наши соц сети: '
        bot.edit_message_text(text=text, chat_id=call.message.chat.id, message_id=call.message.message_id,reply_markup=full_socials)
    if call.data == 'information':
        information = types.InlineKeyboardMarkup()
        fignya_yakas = types.InlineKeyboardButton('Назад', url='https://www.instagram.com/')
        information.add(fignya_yakas)
        text = 'Привет, я - бот, дальше мне лень писать '
        bot.edit_message_text(text=text, chat_id=call.message.chat.id, message_id=call.message.message_id,reply_markup=information)

if __name__ == '__main__':
    bot.polling(none_stop=True)