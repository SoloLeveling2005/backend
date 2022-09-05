import json

import requests

res = requests.get("http://api.weatherapi.com/v1/current.json?key=6983a9ccedfe4ef088e152119220509&q=Astana")
data = res.json()

json_data = json.dumps(data, indent=3)
print(json_data)

print("Страна: ", data['location']['country'])
print("Регион: ", data['location']['region'])
print("Дата:", data['location']['localtime'].split(" ")[0])
print("Время:", data['location']['localtime'].split(" ")[1])
print("Температура по Цельсию: ", data['current']['temp_c'])
print("Скорость ветра: ", data['current']['wind_kph'], "км/ч")
