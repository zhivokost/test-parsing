import requests
from bs4 import BeautifulSoup
r = requests.get("https://market.yandex.ru/catalog--smartfony/26893750/list?text=iphone%208&cvredirect=3&hid=91491&track=srch_visual&onstock=0&local-offers-first=0")
html = BeautifulSoup(r.content)
print(html)
# prices = html.find_all("span", {"class": "_1u3j_pk1db"})
