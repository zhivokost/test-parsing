import requests
from bs4 import BeautifulSoup
r = requests.get("https://video.ittensive.com/data/018-python-advanced/beru.ru/")
html = BeautifulSoup(r.content, features="lxml")
page_href_263 = html.find("img",{"alt": "Холодильник Саратов 263 (КШД-200/30)"}).find_previous("a")
page_href_452 = html.find("img",{"alt": "Холодильник Саратов 452 (КШ-120)"}).find_previous("a")

def find_volume(link):
    volume = 0
    r = requests.get("https://video.ittensive.com/data/018-python-advanced/beru.ru/" + link)
    html = BeautifulSoup(r.content, features="lxml")
    detail = html.find(text="Коротко о товаре").find_all_next("li")[2].find("span").get_text()
    # volume = int(''.join(i for i in detail if i.isdigit()))
    if detail[:11] == 'общий объем':
        volume = int(detail[12:detail.find(' л')].strip())
    return volume

print(f'На {abs(find_volume(page_href_263["href"]) - find_volume(page_href_452["href"]))} л. отличается объемы холодильников Саратов 263 и Саратов 452')

