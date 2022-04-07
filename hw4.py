import requests
from bs4 import BeautifulSoup
import sqlite3

'''
def find_specifications(link):
    headers = {"User-Agent": "ittensive-python-courses/1.0 (+https://www.ittenasive.com)"}
    r = requests.get("https://video.ittensive.com/data/018-python-advanced/beru.ru/" + link, headers=headers)
    html = BeautifulSoup(r.content, features="lxml")
    title = html.find("h1", {"class": "_3TfWusA7bt _26mXJDBxtH"}).get_text()
    price = html.find("span", {"data-tid": "c3eaad93"}).get_text()
    dimensions = ''
    overall_volume = ''
    refrigerate_volume = ''
    for attr in html.find_all("span", {"class": "_112Tad-7AP"}):
        if str(attr).find("ШхВхГ:") > -1:
            dimensions = attr.get_text()
            dimensions = dimensions[dimensions.find(':') + 1: dimensions.find('см')].strip()
            # lec version
            # dimensions = dimensions.split(":")[1].split("x")
            # width = float(dimensions[0])
            # height = float(dimensions[2].split(" ")[0])
        if str(attr).find("общий объем") > -1:
            overall_volume = attr.get_text()
            overall_volume = overall_volume[overall_volume.find('м') + 1: overall_volume.find('л')].strip()
        if str(attr).find("объем холодильной камеры") > -1:
            refrigerate_volume = attr.get_text()
            refrigerate_volume = refrigerate_volume[refrigerate_volume.find('ы') + 1: refrigerate_volume.find(' л')].strip()
    return [link, title, price, dimensions, overall_volume, refrigerate_volume]


headers = {"User-Agent": "ittensive-python-courses/1.0 (+https://www.ittenasive.com)"}
r = requests.get("https://video.ittensive.com/data/018-python-advanced/beru.ru/", headers=headers)
html = BeautifulSoup(r.content, features="lxml")
links = html.find_all("a", {"class": "_3ioN70chUh Usp3kX1MNT _3Uc73lzxcf"})
specifications = []
for link in links:
    if str(link).find("Саратов") > -1:
        specifications.append(find_specifications(link["href"]))

'''

conn = sqlite3.connect("c:\docs\sqlite\data.db3")
db = conn.cursor()

'''
db.execute("""DROP TABLE beru_goods""")
conn.commit()

db.execute("""CREATE TABLE beru_goods  
                (id INTEGER PRIMARY KEY AUTOINCREMENT not null,
                url text,
                title text default '',
                price integer default 0,
                dimensions text default 0, 
                overall integer default 0, 
                refrigerate integer default 0)""")
conn.commit()


for spec in specifications:
    db.execute("INSERT INTO beru_goods (url, title, price, dimensions, overall, refrigerate) VALUES (?, ?, ?, ?, ?, ?)",
               (spec[0], spec[1], spec[2].replace(" ",""), spec[3], spec[4], spec[5]))
    conn.commit()
'''

records = db.execute("SELECT dimensions FROM beru_goods WHERE title LIKE '%Саратов 264%' LIMIT 1").fetchall()
print('Ширина холодильника Саратов 264:', records[0][0][:records[0][0].find('х')], 'см')


db.close()
