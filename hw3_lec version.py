import requests
from bs4 import BeautifulSoup
headers = {"User-Agent": "ittensive-python-courses/1.0 (+https://www.ittenasive.com)"}
r = requests.get("https://video.ittensive.com/data/018-python-advanced/beru.ru/", headers=headers)
html = BeautifulSoup(r.content, features="lxml")
links = html.find_all("a", {"class": "grid-snippet__react-link"})
for link in links:
    if str(link).find("Саратов 263") > -1:
        link_263 = link["href"]
    if str(link).find("Саратов 452") > -1:
        link_452 = link["href"]

def find_volume(link):
    r = requests.get("https://video.ittensive.com/data/018-python-advanced/beru.ru/" + link_263, headers=headers)
    html = BeautifulSoup(r.content, features="lxml")
    volume = html.find_all("span", {"class": "_112Tad-7AP"})
    return int(''.join(i for i in volume[2].get_text() if i.isdigit()))

if link_263 and link_452:
    volume_263 = find_volume(link_263)
    volume_452 = find_volume(link_452)
    diff = max(volume_263, volume_452) - min(volume_263, volume_452)
    print(diff)