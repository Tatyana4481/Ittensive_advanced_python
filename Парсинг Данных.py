import pandas as pd
import requests
from bs4 import BeautifulSoup

r = requests.get(
    "https://mfd.ru/marketdata/?id=5&group=16&mode=3&sortHeader=name&sortOrder=1&selectedDate=01.11.2019")
html = BeautifulSoup(r.content)
table = html.find('table', {'id': 'marketDataList'})
rows = []
trs = table.find_all('tr')
for tr in trs:
    tr = [td.get_text(strip=True) for td in tr.find_all('td')]
    if len(tr) > 0:
        rows.append(tr)
data = pd.DataFrame(rows, columns=["Тикер", "Дата", "Сделки", "C/рост",
                    "С/%", "Закрытие", "Открытие", "min", "max", "avg", "шт",
                                   "руб", "Всего"])
data = data[data["Сделки"] != "N/A"]
data["С/%"] = data["С/%"].str.replace("−",
                                      "-").str.replace("%", "").astype(float)
data = data.set_index("С/%")
data = data.sort_index(ascending=False)
print(data["Тикер"].head(1))
