import telebot

import safe
from audio import handle_voice

bot = telebot.TeleBot(safe.bot_token)
print("asd")


@bot.message_handler(content_types=['text'])
def text_handler(message):
    chat_id = message.chat.id
    print(f"Msg recieved from {chat_id}")
    bot.send_message(chat_id, "Отправьте мне голосовое сообщение, и я сделаю вашу жизнь чуточку лучше!")


@bot.message_handler(content_types=['voice'])
def audio_handler(message):
    recognized = handle_voice(message, bot, safe.bot_token)
    bot.reply_to(message, recognized)


print("asd")
bot.polling(none_stop=True)
print("asd")
