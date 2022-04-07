import requests
request = requests.get("https://geocode-maps.yandex.ru/1.x/?apikey=075ae6af-d914-476d-a402-2bbd183e1dcd&geocode=Самара")
import xml.etree.ElementTree as ET
root = ET.fromstring(request.text)
data = root[0][1][0][4][0].text
print('Долгота точки города Самара:', data.split()[0])



import json
request = requests.get("https://geocode-maps.yandex.ru/1.x/?apikey=075ae6af-d914-476d-a402-2bbd183e1dcd&geocode=Самара&format=json&results=1")
geo = json.loads(request.content)
print('Вариант учителя: ',geo['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].split()[0])
