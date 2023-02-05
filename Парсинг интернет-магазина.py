import requests
from bs4 import BeautifulSoup
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 YaBrowser/19.12.0.358 Yowser/2.5 Safari/537.36"}
r = requests.get("https://beru.ru/search?cvredirect=2&suggest_reqId=27865074762321487883702093457804&text=%D1%81%D0%B0%D1%80%D0%B0%D1%82%D0%BE%D0%B2", headers=headers)
html = BeautifulSoup(r.content)
print(r.content)
links = html.find_all("a", {"class": "grid-snippet__react-link"})
link_263 = ''
link_452 = ''
for link in links:
    if str(link).find("Саратов 263") > -1:
        link_263 = link["href"]
    if str(link).find("Саратов 452") > -1:
        link_452 = link["href"]


def find_volume(link):
    r = requests.get("https://beru.ru" + link)
    html = BeautifulSoup(r.content)
    volume = html.find_all("span", {"class": "_112Tad-7AP"})
    return int(''.join(i for i in volume[2].get_text() if i.isdigit()))


if link_263 and link_452:
    volume_263 = find_volume(link_263)
    volume_452 = find_volume(link_452)
    diff = max(volume_263, volume_452) - min(volume_263, volume_452)
    print(diff)
