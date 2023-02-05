import json
import pandas as pd
import requests
request = requests.get("https://www.cbr-xml-daily.ru/daily_json.js")
data = request.text
data = pd.DataFrame(json.loads(data)["Valute"])
print(data["USD"]["Value"]/data["USD"]["Nominal"])
