import requests
import pandas as pd
from bs4 import BeautifulSoup
# получаем данные со страницы
r = requests.get("https://mfd.ru/marketdata/?id=5&group=16&mode=3&sortHeader=name&sortOrder=1&selectedDate=01.11.2019")

# преобразуем данные с помощью библиотеки BeautifulSoup
html = BeautifulSoup(r.content, features="lxml")
data = []
table = html.find("table", {'id':'marketDataList'})
for tr in table.find_all("tr"):
      data.append([td.get_text().replace('%','').replace('+','').replace('−','-') for td in tr.find_all("td")])
data = pd.DataFrame(data[2:])

# отберем необходимые данные: наименование тикера и процентное изменение числа сделок
data = data[[0,4]].rename(columns={0: "Тикер", 4: "Изменение числа сделок"})
data.dropna(how='any', inplace=True)
data.drop(data[data["Изменение числа сделок"]==''].index, inplace=True)

# приводим значения изменения числа сделок в процентак к типу данных 'float'
data["Изменение числа сделок"] = data["Изменение числа сделок"].apply(lambda x: float(x))

# находим максимальное изменение числа сделок
print(data[data["Изменение числа сделок"]==data["Изменение числа сделок"].max()])