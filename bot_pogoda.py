import telebot
import requests



bot = telebot.TeleBot('5619246297:AAH1C-8T3SYWIDlcdgF_Ys2N9F5jSxCeSvQ')

@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/start':
        bot.send_message(message.from_user.id, "введите город: ")
        bot.register_next_step_handler(message, pogoda)
    else:
        bot.send_message(message.from_user.id, 'Напиши /start')

def pogoda(message):
    name = message.text
    response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={name}&appid=4321a3d417b53045aa1b6617c529c910&units=metric&lang=ru")
    weather = response.json()['weather'][0]['description']
    temp = response.json()['main']['temp']
    temp_feeling = response.json()['main']['feels_like']
    bot.send_message (message.from_user.id, f'погода в городе {name}:\n{weather}, температура воздуха - {temp}, ощущается как {temp_feeling}')
# # Запускаем бота
bot.polling(none_stop=True, interval=0)



# Функция, обрабатывающая команду /start
# @bot.message_handler(commands=["start"])
# def start(m, res=False):
#     # c.button_click()
#     bot.send_message(m.chat.id, 'Я на связи. Напиши мне что-нибудь )')
# # Получение сообщений от юзера
# @bot.message_handler(content_types=["text"])
# def handle_text(message):
#     bot.send_message(message.chat.id, 'Вы написали: ' + message.text)
# # Запускаем бота
# bot.polling(none_stop=True, interval=0)