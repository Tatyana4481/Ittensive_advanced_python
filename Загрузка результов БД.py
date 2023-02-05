import sqlite3
import requests
from bs4 import BeautifulSoup

def find_number(text):
    return int("0" + "".join(i for i in text if i.isdigit()))
def find_data (link):
    r = requests.get("https://beru.ru" + link)
    html = BeautifulSoup(r.content)
    title = html.find("h1", {"class": "_3TfWusA7bt"}).get_text()
    price = find_number(html.find("span", {"data-tid": "c3eaad93"}).get_text())
    tags = html.find_all("span", {"class": "_112Tad-7AP"})
    width = 0
    depth = 0
    height = 0
    volume = 0
    freezer = 0
    for tag in tags:
        tag = tag.get_text()
        if tag.find("ШхВхГ") > -1:
            dims = tag.split(":")[1].split("х")
            width = float(dims[0])
            depth = float(dims[1])
            height = float(dims[2].split(" ")[0])
        if tag.find("общий объем") > -1:
            volume = find_number(tag)
        if tag.find("объем холодильной камеры") > -1:
            freezer = find_number(tag)
    return [link, title, price, width, depth, height, volume, freezer]

r = requests.get("https://beru.ru/catalog/kholodilniki/79958/list?cvredirect=3&suggest_reqId=83526016473955609954771572320629&text=%D0%A1%D0%B0%D1%80%D0%B0%D1%82%D0%BE%D0%B2")
html = BeautifulSoup(r.content)
links = html.find_all("a", {"class": "grid-snippet__react-link"})
data = []
for link in links:
    if link["href"] and link.get_text().find("Саратов") > -1:
        data.append(find_data(link["href"]))
conn = sqlite3.connect("sqlite/data.db3")
db = conn.cursor()
db.execute("""CREATE TABLE beru_goods
            (id INTEGER PRIMARY KEY AUTOINCREMENT not null,
            url text,
            title text default '',
            price INTEGER default 0,
            width FLOAT default 0.0,
            depth FLOAT default 0.0,
            height FLOAT default 0.0,
            volume INTEGER default 0,
            freezer INTEGER default 0)""")
conn.commit()
db.executemany("""INSERT INTO beru_goods (url, title, price, width, depth, height, volume, freezer)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?)""", data)
conn.commit()
print (db.execute("SELECT * FROM beru_goods").fetchall())
db.close()
