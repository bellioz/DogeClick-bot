from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from telethon import TelegramClient, events, sync
import random
import time

# Инициализация сессии
options = Options()
options.headless = True

# ID и Hash Telegram клиента
api_id = 1234567
api_hash = '1234a5b67c89012d345ef6789gh01i23'

# Инициализация клиента
client = TelegramClient('doge_bot', api_id, api_hash)

# Username бота с которым работаем
username = '@Dogecoin_click_bot'

urls = []

while(True):
    try:
        # Подключение клиента
        client.connect()
        driver = webdriver.Chrome(options=options)

        # Случайное число секунд в диапазоне 70-120
        seconds = random.randint(70, 120)

        # Последнее сообщение
        message = client.get_messages(username)

        # Текст последнего сообщения
        text = message[0].message

        # Ссылка в последнем сообщении
        try:
            url = message[0].buttons[0][0].url
        except Exception:
            url = None
        if url in urls:
            print('Ссылка устарела, отправляю команду /visit')
            client.send_message(username, "/visit")
            continue
        else:
            urls.clear()

        # Если есть ссылка то переходим
        if url is not None:
            print('Перехожу по ссылке:', url)
            driver.get(url)
            urls.append(url)
            time.sleep(seconds)
            driver.quit()

        # Если нет, то ждем, а затем отправляем команду /visit
        else:
            wait = random.randint(3600, 7200)
            print('Ссылки закончились, таймаут на ' + str(wait) + ' секунд')
            driver.quit()
            time.sleep(wait)
            client.send_message(username, "/visit")
            time.sleep(10)

        # Отключение клиента
        client.disconnect()

    except Exception as e:
        print('Ошибка:', e)
        time.sleep(10)
        pass
