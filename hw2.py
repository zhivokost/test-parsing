import requests
import pandas as pd
from bs4 import BeautifulSoup
r = requests.get("http://mfd.ru/marketdata/?id=5&group=16&mode=3&sortHeader=name&sortOrder=1&selectedDate=01.11.2019")
html = BeautifulSoup(r.content, features="lxml")
data = []
tiker_stat = []
table = html.find("table", {"class": "mfd-table", "id": "marketDataList"})
table = table.find_all("tbody")[1]
for tr in table.find_all("tr"):
    data.append([td.get_text() for td in tr.find_all("td")])
for list1 in data:
    if str(list1[4]) != '' and str(list1[4])[0] == '+':
        tiker_stat.append([list1[0],list1[4]])
data = pd.DataFrame(tiker_stat, columns=['Тикер','Процент сделок'])
data['Процент сделок'] = data['Процент сделок'].str.replace("%","").astype(float)
print('Максимальный рост числа сделок (в процентах) за 1 ноября 2019 года у Тикера:')
print(data[data['Процент сделок'] == data['Процент сделок'].max()])
