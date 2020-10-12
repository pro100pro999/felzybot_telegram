#-*- coding: utf-8 -*-
import telebot
import configure
from glob import glob
from random import choice
from telebot import types
client = telebot.TeleBot(configure.config['token'])

    

@client.message_handler(commands = ['about','info','help'])
def get_user_info(message):
    markup_inline = types.InlineKeyboardMarkup()
    item_donat = types.InlineKeyboardButton(text= 'Донат',callback_data='donat')
    item_streams = types.InlineKeyboardButton(text= 'Стримы',callback_data='streams')
    item_discord = types.InlineKeyboardButton(text= 'Наш дискорд сервер',callback_data='discord')
    item_contacts = types.InlineKeyboardButton(text= 'Контакты для связи',callback_data='contacts')
    markup_inline.add(item_donat,item_streams,item_discord,item_contacts)
    client.send_message(message.chat.id, 'Какую информацию вы хотите узнать?',
                        reply_markup = markup_inline)

@client.callback_query_handler(func = lambda call: True)
def answer(call):
    if call.data == 'donat':
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)
        item_id = types.KeyboardButton('Помогло.')
        item_username = types.KeyboardButton('Не помогло.')
        markup_reply.add(item_id, item_username)
        client.send_message(call.message.chat.id, '-------------------------------------------')
        client.send_message(call.message.chat.id, 'Очень мило,что ты решил помочь нам :3. Донат мы принимаем только на киви. Вот ссылка - ...',
                            reply_markup = markup_reply)
        client.send_message(call.message.chat.id, 'Если я тебе помог,пожалуйста,оставь отзыв,нажав на кнопку ниже.',
                                    reply_markup = markup_reply)        
    elif call.data == 'streams':
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)
        item_id = types.KeyboardButton('Помогло.')
        item_username = types.KeyboardButton('Не помогло.')
        markup_reply.add(item_id, item_username)
        client.send_message(call.message.chat.id, '-------------------------------------------')
        client.send_message(call.message.chat.id, 'Стримы пока что проводиться не будут.',
                                    reply_markup = markup_reply)
        client.send_message(call.message.chat.id, 'Если я тебе помог,пожалуйста,оставь отзыв,нажав на кнопку ниже.',
                                            reply_markup = markup_reply)    
    elif call.data == 'discord':
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)
        item_id = types.KeyboardButton('Помогло.')
        item_username = types.KeyboardButton('Не помогло.')
        markup_reply.add(item_id, item_username)
        client.send_message(call.message.chat.id, '-------------------------------------------')
        client.send_message(call.message.chat.id, 'Наш дискорд сервер - ... Там ты можешь напрямую задать вопросы нашему любимому ютуберу ;)',
                                            reply_markup = markup_reply)
        client.send_message(call.message.chat.id, 'Если я тебе помог,пожалуйста,оставь отзыв,нажав на кнопку ниже.',
                                                    reply_markup = markup_reply)  
    elif call.data == 'contacts':
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)
        item_id = types.KeyboardButton('Помогло.')
        item_username = types.KeyboardButton('Не помогло.')
        markup_reply.add(item_id, item_username)
        client.send_message(call.message.chat.id, '-------------------------------------------')
        client.send_message(call.message.chat.id, 'Контакты для связи: Telegram - @IamFelzy' ,
                                                    reply_markup = markup_reply)
        client.send_message(call.message.chat.id, 'Если я тебе помог,пожалуйста,оставь отзыв,нажав на кнопку ниже.',
                                                            reply_markup = markup_reply)    


@client.message_handler(content_types = ['text'])
def get_text(message):
    if message.text.lower() == '/start':
        client.send_message(message.chat.id, 'Привет! Я бот ютубера Felzy(он кстати мой создатель). Я выполняю функции помощника. Пропиши /help для просмотра моих команд.')
    if message.text == 'Помогло.':
        client.send_message(message.chat.id, 'Спасибо,я знал,что мы найдем с тобой общий язык :3')
        lists = glob('img/*')
        picture = choice(lists)
        client.send_photo(message.chat.id, photo = open(picture, 'rb'))
    elif message.text == 'Не помогло.':
        client.send_message(message.chat.id, 'Жаль. Я ведь пытался тебе помочь =(. Но спасибо,что помогаешь делать меня лучше.')
        lists = glob('img2/*')
        picture = choice(lists)
        client.send_photo(message.chat.id, photo = open(picture, 'rb'))        
    
client.polling(none_stop = True, interval = 0)