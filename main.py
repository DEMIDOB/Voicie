import telebot

import safe

bot = telebot.TeleBot(safe.bot_token)


@bot.message_handler(content_types=['text'])
def text_handler(message):
    chat_id = message.chat.id
    print(f"Msg recieved from {chat_id}")
    bot.send_message(chat_id, "Отправьте мне голосовое сообщение, и я сделаю вашу жизнь чуточку лучше! 😉")


bot.polling(none_stop=True)
