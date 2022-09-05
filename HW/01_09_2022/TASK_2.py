import sys
import threading
import time

import requests
from bs4 import BeautifulSoup
import json
import re

print("Скачаем все картинки с любого сайта (на самом деле не со всех)")
print("Сайты с которых картинки скачиваются: 'https://wallpaperscraft.ru/', 'https://yandex.kz/images/', "
      "'https://fonwall.ru/', 'https://nicefon.ru/downloads.html', https://www.goodfon.ru/")
print("Сайты с которых картинки НЕ скачиваются: 'https://pixabay.com/ru/', 'https://zastavok.net/', "
      "'https://akspic.ru/album/1920x1080'")
url = input("Введите ссылку на страницу для скачивания картинки: ")

# response = requests.get('https://wallpaperscraft.ru/',
#                      headers={'user-agent': 'my-agent-0.0.1'},
#                      cookies={'one': 'true'})
# response = requests.get('https://yandex.kz/images/',
#                      headers={'user-agent': 'my-agent-0.0.1'},
#                      cookies={'one': 'true'})
# response = requests.get('https://fonwall.ru/',
#                      headers={'user-agent': 'my-agent-0.0.1'},
#                      cookies={'one': 'true'})
# response = requests.get('https://pixabay.com/ru/',     НЕ СКАЧИВАЕТСЯ
#                      headers={'user-agent': 'my-agent-0.0.1'},
#                      cookies={'one': 'true'})
# response = requests.get('https://nicefon.ru/downloads.html',
#                      headers={'user-agent': 'my-agent-0.0.1'},
#                      cookies={'one': 'true'})
# response = requests.get('https://zastavok.net/',     НЕ СКАЧИВАЕТСЯ
#                      headers={'user-agent': 'my-agent-0.0.1'},
#                      cookies={'one': 'true'})
# response = requests.get('https://www.goodfon.ru/',
#                         headers={'user-agent': 'my-agent-0.0.1'},
#                         cookies={'one': 'true'})
# response = requests.get('https://akspic.ru/album/1920x1080',
#                      headers={'user-agent': 'my-agent-0.0.1'},
#                      cookies={'one': 'true'})


response = requests.get(str(url),
                        headers={'user-agent': 'my-agent-0.0.1'},
                        cookies={'one': 'true'})

soup = BeautifulSoup(response.content, "html.parser")
imgs = soup.find_all("img")
# print(imgs)
# print("\n\n\n\n")


def download(i, ii):
    img_data = requests.get(i['src']).content
    with open(f'{ii}.jpg', 'wb') as handler:
        handler.write(img_data)
    # print(i['src'])


ii = 0
for i in imgs:
    if "https" in str(i['src']):
        t = threading.Thread(target=download, args=(i, ii))
        t.start()
        ii += 1

animation = ["■□□□□□□□□□", "■■□□□□□□□□", "■■■□□□□□□□", "■■■■□□□□□□", "■■■■■□□□□□", "■■■■■■□□□□", "■■■■■■■□□□",
             "■■■■■■■■□□", "■■■■■■■■■□", "■■■■■■■■■■", ""]

print("\nНачинаю скачивание")
for i in range(len(animation)):
    time.sleep(.2)
    sys.stdout.write("\r" + animation[i % len(animation)])
    sys.stdout.flush()

while True:
    time.sleep(.3)
    n_thread = threading.active_count()
    if n_thread == 1:
        print("\nСкачка завершена")
        break
