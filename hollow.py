import telebot
import os
import pickle
import datetime
path = os.getcwd()
print(path)
with open("users.dat", "rb") as f :
    apple = pickle.load(f)
passwords = apple[0]
messages = apple[1]
# with open("users.dat", "rb") as f :
#     users =  #pickle.load(f)
bot = telebot.TeleBot('1836330544:AAG-b8FJi90cPQ0eOXRKv3c7juaQw-HSvNE')
print(len(passwords))
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    print(messages)
    login = message.from_user.username
    passwords.add(message.from_user.username)
    offset = datetime.timezone(datetime.timedelta(hours=3))
    if message.from_user.username not in messages.keys():
        messages[message.from_user.username] = []
    if message.text == "/start":
        bot.send_message(message.from_user.id, 'Привет! Это социальная сеть Hollow! Напишите: /write имя_пользователя сообщение чтобы написать сообщение, /my_username чтобы узнать свой адрес для отправления сообщений и /look для прочитывания сообщений.')
    if "/write" in message.text :
        while True :
            try :
                if message.text.split()[1] in passwords :
                    print("hello")
                    msg = ' '.join(message.text.split()[2:])
                    imac = str(datetime.datetime.now(offset))[:16]
                    messages[message.text.split()[1]].append([login, msg, imac])
                    
                    bot.send_message(message.from_user.id, 'Сообщение отправлено!')
                    with open("users.dat", "wb") as qw :
                        pickle.dump([passwords, messages], qw)
                    break
                else :
                    bot.send_message(message.from_user.id, 'Этого пользователя не существует!')
                    break
            except :
                bot.send_message(message.from_user.id, 'Используйте синтаксис! /write имя_пользователя сообщение')
                break
    if message.text == "/look" :
        for i in list(messages.items()) :
            if i[0] == login :
                for j in i[1] :
                    bot.send_message(message.from_user.id, f'''{j[0]} написал: {j[1]}     
                    Дата и время отправки: {j[2]}''')
    if message.text == "/my_username" :
        bot.send_message(message.from_user.id, message.from_user.username)
bot.polling(none_stop=True, interval=1)