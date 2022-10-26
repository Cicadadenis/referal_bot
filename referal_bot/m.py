import sqlite3
from re import findall
from threading import Timer
from threading import *
from aiogram import Dispatcher, executor
from aiogram.dispatcher.filters import ChatTypeFilter
from aiogram.types import (ChatType, ContentTypes, InlineKeyboardButton,
                        InlineKeyboardMarkup, Message)
from io import BytesIO
from PIL import Image,  ImageDraw, ImageFont
import secrets
import aiohttp
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, Message
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import Bot, types
from aiogram.utils.markdown import hbold, hlink
from aiogram.utils.exceptions import BadRequest
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from rich.logging import RichHandler
from datetime import datetime, date, time
import sqlite3
import random
from pathlib import Path
from os.path import exists
from datetime import datetime
import requests, os
from requests_html import HTMLSession
import asyncio, time
from aiogram.types import User
import time
from threading import Timer
import asyncio
import sys
import re
import pyshorteners
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, inline_keyboard
dirr = os.listdir()
if "token.txt" not in  dirr:
    ttt = input("\n\nТокен Бота:    ")
    with open('token.txt', 'w', encoding="utf-8") as f:
        f.write(ttt)
cicada_kb = InlineKeyboardMarkup()
cicada_kb.add(
    InlineKeyboardButton('➕ Добавить Ботов', callback_data='addd'),
    InlineKeyboardButton('➖ Удалить Ботов', callback_data='delll')
)

token= open('token.txt', 'r').read()

re = "\033[1;31m"
gr = "\033[1;32m"
cy="\033[1;36m"

logo = (
            f"                    _             __         {re}___       __{cy}\n"
            f"               ____(_)______ ____/ /__ _____{re}/ _ )___  / /_{cy}\n"
            f"              / __/ / __/ _ `/ _  / _ `/___{re}/ _  / _ \/ __/{cy}\n"
            f"              \__/_/\__/\_,_/\_,_/\_,_/   {re}/____/\___/\__/{cy}\n"
            f"              ----------Telegram-Bot-Cicada3301-----------\n\n"
)
re = "\033[1;31m"
gr = "\033[1;32m"
cy = "\033[1;36m"
MethodGetMe = (f'''https://api.telegram.org/bot{token}/GetMe''')
response = requests.post(MethodGetMe)
tttm = response.json()
tk = tttm['ok']
if tk == True:
    id_us = (tttm['result']['id'])
    first_name = (tttm['result']['first_name'])
    username = (tttm['result']['username'])
    uurl = f"https://t.me/{username}"
    s = pyshorteners.Shortener()
    pr9 = (s.dagd.short(uurl))
    os.system('cls')
    print(logo)

    print(f"""
                ---------------------------------
                🆔 Bot id: {id_us}
                ---------------------------------
                👤 Имя Бота: {first_name}
                ---------------------------------
                🗣 username: {username}
                ---------------------------------
                🌐 {pr9}
                ---------------------------------
                ******* Suport: @Satanasat ******
    """)

class cicada(StatesGroup):
    sms = State()

class akasil(StatesGroup):
    sms_text = State()
    search = State()
    urlses = State()
    parser = State()
baza = []
ps = []
spisok = []
y = []
botttt = []
if "bots.txt" not in  dirr:
    open('bots.txt', 'w')
bots = open("bots.txt", "r").readlines()
print(len(bots))
if len(bots) >= 2:
    for bott in bots:
        bott = bott.split("\n")[0]
        botttt.append(bott)
print(len(botttt))
bot = Bot(token=token, parse_mode="HTML")
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(text="//admin", state="*")
async def adm(message: types.Message, state: FSMContext):
    await message.answer(f"📢 <b>Меню Администратора !!!</b>", reply_markup=cicada_kb)
    await state.finish()

@dp.callback_query_handler(text="delll", state="*")
async def ref(call: CallbackQuery, state: FSMContext):
    botttt.clear()
    await state.finish()
    open("bots.txt", 'w')
    baza.clear()
    botttt.clear()
    spisok.clear()
    await call.message.answer("📢 <b>Список Ботов Очищен !!!</b>")

@dp.callback_query_handler(text="addd", state="*")
async def ref(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.answer("📢 <b>Введите Список Юзиков Каждый С Новой Строки:</b>")
    await akasil.sms_text.set()



@dp.message_handler(state=akasil.sms_text)
async def input_text_for_ad(message: types.Message, state: FSMContext):
    ff = message.text
    ls = ff.split('\n')
    botttt.clear()
    for x in ls:
        if x.split('https://t.me/'):
            xxx = x.split('https://t.me/')[-1]
            if xxx.split('@'):
                xxx = xxx.split('@')[-1]
        botttt.append(xxx)
        with open("bots.txt", "a", encoding='utf-8') as f:
            f.write(f"{xxx}\n")
    await state.finish()
    baza.clear()
    spisok.clear()
    await message.answer(f"📢 <b>Было Добавленно {len(ls)} Ботов !!!</b>")

@dp.message_handler(commands=['start'], state="*")
async def show_contact(message: types.Message, state: FSMContext):
    #await state.finish()
    ps.clear()
    chat_id = message.chat.id
    password = secrets.token_urlsafe(3)
    ps.append(password)
    im = Image.open('dropbox-logo@2x.jpg')
    draw_text = ImageDraw.Draw(im)
    font = ImageFont.truetype('Carnivale.ttf', size=170)
    draw_text.text(
        (220,120),
        password,
        font=font,
        fill=('green'),
        colors='green'
        )
    im.save('new_pic.jpg')
    pp = open("new_pic.jpg", 'rb').read()
    text = (f"<b>Введите код с картинки 👆</b>\n"
           f" ➖➖➖➖➖➖➖➖➖\n"
           f"<b>Чтобы вернуться в меню и начать</b>\n"
           f"<b>Oтправьте 👉 /start</b>")
    await bot.send_photo(chat_id, photo=pp, caption=text)
    await cicada.sms.set()


@dp.message_handler(state=cicada.sms)
async def b6ot2(message: Message, state):
    async def mmm():
        def nowi():
            if len(botttt) >= 1:
                while True: 
                    msg = random.choice(botttt)
                    session = HTMLSession()
                    r = session.get(f'https://t.me/{msg}')
                    
                    if '<i class="tgme_icon_user"></i>' not in r.text:
                        return msg
                        break
            else:
                hhh = 'xxx'
                return hhh
        def starii():
            for x in spisok:
                xx = int(x.split(':')[0])
    
                if xx == chat_id:
                    msg = x.split(":")
                
                    session = HTMLSession()
                    r = session.get(f'https://t.me/{msg[1]}')
                
                    if '<i class="tgme_icon_user"></i>' not in r.text:

                        return msg[1]
                    else:

                        sss = nowi()
                        baza.remove(chat_id)
                        spisok.remove(f"{msg[0]}:{msg[1]}")
                        return sss
        chat_id = message.chat.id
        if chat_id in baza:
            msg = starii()
            baza.append(chat_id)
            do_spiska = f"{chat_id}:{msg}"
            spisok.append(do_spiska)
            await message.answer(f"<b>✳️ Привет {message.from_user.first_name} ✳️</b>\n\n"
                                f"➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                                f"<b>твой Бот: <a href='http://t.me/{msg}'>@{msg}</a> Жив</b>\n\n"
                                f"➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                                f"<b>Если Тот Умрет Вернись Сюда И Получишь Новый:</b>")
        if chat_id not in baza:
            bot = nowi()
            if "xxx" not in bot:
        
                baza.append(chat_id)
                do_spiska = f"{chat_id}:{bot}"
                spisok.append(do_spiska)
                        
                await message.answer(f"<b>✳️ Привет {message.from_user.first_name} ✳️</b>\n\n"
                                    f"➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                                    f"<b>Вот твой Бот: <a href='http://t.me/{bot}'>@{bot}</a></b>\n\n"
                                    f"➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                                    f"<b>Если Тот Умрет Вернись Сюда И Получишь Новый:</b>")
            else:
                await message.answer("<b>Боты Скоро Появяться</b>")
    chat_id = message.chat.id
    pas = message.text
    if pas == ps[0]:
        ps.clear()
        await mmm()

    else:
        await message.answer("<b>Неверно Введена Капча\nПопробуйте Снова</b>")
        await show_contact(message, state="*")




if __name__ == '__main__':
    executor.start_polling(dp)
