import sqlite3
import requests
from bs4 import BeautifulSoup

conn = sqlite3.connect("c:\docs\sqlite\data.db3")
db = conn.cursor()

films = db.execute("SELECT id, url FROM films WHERE title='' LIMIT 1").fetchall()
for film in films:
    headers = {"User-Agent": "ittensive-python-scrapper/1.0 (+https://www.ittenasive.com)"}
    r = requests.get("https://www.kinopoisk.ru" + film[1], headers=headers)
    html = BeautifulSoup(r.content, features="lxml")
    title = html.find("span", {"class": "moviename-title-wrapper"}).get_text()
    tags = html.find_all("td", {"class": "dollar"})
    budget = 0
    sales_www = 0
    if len(tags) > 0:
        sales_www = tags[0].get_text()
        if len(tags) > 1:
            budget = tags[0].get_text()
            sales_www = tags[::-1][0].get_text()
            if len(tags) > 2:
                sales_www = tags[2].get_text()
    budget = int("0" + ''.join(i for i in budget if i.isdigit()))
    if sales_www.find("+") > -1:
        sales_www = sales_www.split("=")[1]
    sales_www = int("0" + ''.join(i for i in sales_www if i.isdigit()))

    db.execute("UPDATE films SET title=?, budget=?, sales_www=? WHERE id=?",
               (title, budget, sales_www, film[0]))

conn.commit()

db.close()
