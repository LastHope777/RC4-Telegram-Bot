# RC4 Telegram Bot 🔐

![Python](https://img.shields.io/badge/Python-3.11-blue.svg)
![pyTelegramBotAPI](https://img.shields.io/badge/pyTelegramBotAPI-4.x-blue.svg)
![License](https://img.shields.io/badge/license-MIT-orange.svg)

**RC4 Telegram Bot** — бот для шифрования и расшифровки текста с использованием классического потокового шифра **RC4**.  

Разработан студентами группы **6402-020302D**: **Никитой Пишковым** и **Егором Мамонтовым** в рамках дисциплины **«Теория информации»**.

---

## Функции бота
- 🔐 Зашифровать текст в HEX  
- 🔓 Расшифровать HEX обратно в текст  
- 🗝 Изменять ключ шифрования  
- ✅ Отдельный ключ для каждого пользователя  
- 💬 Удобное меню с кнопками и emoji  

---
## 🛠️ Технологии
- [Python 3.11+](https://www.python.org/)
- [pyTelegramBotAPI](https://pypi.org/project/pyTelegramBotAPI/) 
- [python-dotenv](https://pypi.org/project/python-dotenv/) 
---
## 📁 Структура проекта
```
RC4-Telegram-Bot/
├── main.py
├── requirements.txt
├── README.md
├── LICENSE
├── .env          # не в репозитории
└── .gitignore
```
---
## Установка и запуск
1. Клонируйте репозиторий:

```bash
git clone https://github.com/LastHope777/RC4-Telegram-Bot.git
cd RC4-Telegram-Bot
```

2. Создайте виртуальное окружение и установите зависимости:

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\\Scripts\\activate      # Windows
```

3. Создайте файл `.env` в корне проекта и добавьте токен вашего бота:

```
TOKEN=ваш\_токен\_от\_BotFather
```

> ⚠ Никогда не выкладывайте `.env` в публичный репозиторий.  

4. Запустите бота:

```bash
python main.py
```

---

## Использование
- `/start` — запуск бота  
- Кнопки меню: 🔐 Зашифровать, 🔓 Расшифровать, 🗝 Изменить ключ  

---

## Пример работы
<img width="393" height="809" alt="iPhone 14 Pro Max-Photoroom" src="https://github.com/user-attachments/assets/91b053af-d57d-44b9-927c-f4fb589d81ab" />

---

## Примечания
- RC4 **устарел** и не рекомендуется для реального шифрования, этот бот создан **в образовательных целях**.  
- Каждый пользователь может использовать свой ключ.

---

## Лицензия
MIT [LICENSE](LICENSE)

