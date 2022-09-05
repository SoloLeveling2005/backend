import requests
from bs4 import BeautifulSoup
import json
import re

'''
Я знаю что может кода многовато, но 
'''

response = requests.get('https://kurs24.kz/')
# print(response.text)
list_currency = []
list_cur = []
list_span = []
soup = BeautifulSoup(response.content, "html.parser")
nbrk = soup.find_all("div", {"class": "nbrk"})
# nbrk__table = nbrk.find_all("div", {"class": "nbrk__table"})
for nbrk__table in nbrk:
    nbrk__table = nbrk__table.find_all("div", {"class": "nbrk__table"})
    # print(nbrk__table)
    for nbrk__table_td in nbrk__table:
        nbrk__table_td = nbrk__table_td.find_all("td")
        # for i in nbrk__table_td:
        #     print(i)
        for nbrk__table_td_currency in nbrk__table_td:
            nbrk__table_td_currency = nbrk__table_td_currency.find("span", {"class": "d-inline d-md-none"})
            # print(nbrk__table_td_a)
            if nbrk__table_td_currency is not None:
                list_currency.append(nbrk__table_td_currency.text)
        for nbrk__table_td_cur in nbrk__table_td:
            nbrk__table_td_cur = nbrk__table_td_cur.find("cur", {"class": "nbrk__currency"})
            if nbrk__table_td_cur is not None:
                # print(nbrk__table_td_cur.type)
                try:
                    list_cur.append(nbrk__table_td_cur.text.replace('\t', '').replace('\n', '').replace('\r', ''))
                except:
                    pass

        for nbrk__table_td_span in nbrk__table_td:
            nbrk__table_td_span = nbrk__table_td_span.find("span", {"nbrk__difference"})
            if nbrk__table_td_span is not None:
                list_span.append(nbrk__table_td_span.text.replace('\t', '').replace('\n', '').replace('\r', ''))

# print(list_currency)
# print(list_cur)
# print(list_span)

for i in range(1, 100):
    try:
        print("1 ", list_currency[i - 1], "", list_cur[i - 1])
    except:
        break
