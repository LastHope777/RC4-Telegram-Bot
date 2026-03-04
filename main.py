import os

import telebot
from dotenv import load_dotenv
from telebot import types

# --------------------- RC4 IMPLEMENTATION --------------------- #
def rc4(key: bytes, data: bytes) -> bytes:
    S = list(range(256))
    j = 0
    out = []

    # KSA
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]

    # PRGA
    i = j = 0
    for char in data:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        K = S[(S[i] + S[j]) % 256]
        out.append(char ^ K)

    return bytes(out)


# --------------------- TELEGRAM BOT --------------------- #

load_dotenv()
TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(TOKEN)

# Храним ключи пользователей в памяти
user_keys = {}


# --------------------- КЛАВИАТУРЫ --------------------- #

def main_menu():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🔐 Зашифровать")
    btn2 = types.KeyboardButton("🔓 Расшифровать")
    btn3 = types.KeyboardButton("🗝 Изменить ключ")
    keyboard.add(btn1, btn2)
    keyboard.add(btn3)
    return keyboard


# --------------------- ОБРАБОТЧИКИ --------------------- #

@bot.message_handler(commands=['start'])
def start(message):
    user_keys[message.chat.id] = "secretkey"

    bot.send_message(
        message.chat.id,
        "👋 Привет!\n"
        "Я бот для шифрования и расшифровки *RC4*.\n\n"
        "Авторы: Никита Пишков, Егор Мамонтов.\n\n"
        "Текущий ключ: `secretkey`\n\n"
        "Выбери действие:",
        parse_mode="Markdown",
        reply_markup=main_menu()
    )


# --------------------- ШИФРОВАНИЕ --------------------- #

@bot.message_handler(func=lambda m: m.text == "🔐 Зашифровать")
def encrypt_start(message):
    bot.send_message(message.chat.id, "Введите текст для шифрования:")
    bot.register_next_step_handler(message, encrypt_do)


def encrypt_do(message):
    key = user_keys.get(message.chat.id, "secretkey").encode()
    plaintext = message.text.encode()
    cipher = rc4(key, plaintext).hex()

    bot.send_message(
        message.chat.id,
        f"🛡 Зашифрованный HEX:\n`{cipher}`",
        parse_mode="Markdown",
        reply_markup=main_menu()
    )


# --------------------- РАСШИФРОВКА --------------------- #

@bot.message_handler(func=lambda m: m.text == "🔓 Расшифровать")
def decrypt_start(message):
    bot.send_message(message.chat.id, "Введите HEX для расшифровки:")
    bot.register_next_step_handler(message, decrypt_do)


def decrypt_do(message):
    try:
        encrypted = bytes.fromhex(message.text)
    except:
        bot.send_message(message.chat.id, "❌ Ошибка: некорректный HEX.")
        return

    key = user_keys.get(message.chat.id, "secretkey").encode()

    decrypted = rc4(key, encrypted).decode(errors='ignore')

    bot.send_message(
        message.chat.id,
        f"📖 Расшифровано:\n`{decrypted}`",
        parse_mode="Markdown",
        reply_markup=main_menu()
    )


# --------------------- ИЗМЕНЕНИЕ КЛЮЧА --------------------- #

@bot.message_handler(func=lambda m: m.text == "🗝 Изменить ключ")
def change_key_start(message):
    bot.send_message(message.chat.id, "Введите новый ключ:")
    bot.register_next_step_handler(message, change_key_do)


def change_key_do(message):
    user_keys[message.chat.id] = message.text.strip()

    bot.send_message(
        message.chat.id,
        f"🔑 Ключ успешно изменён!\nНовый ключ: `{message.text}`",
        parse_mode="Markdown",
        reply_markup=main_menu()
    )


# --------------------- ЗАПУСК --------------------- #

bot.polling(none_stop=True)
