import pandas as pd

data1 = pd.read_csv("https://video.ittensive.com/python-advanced/data-9753-2019-07-25.utf.csv", delimiter=";")
data1 = data1.set_index(["Year", "Period"])
data2 = pd.read_csv("https://video.ittensive.com/python-advanced/data-5283-2019-10-04.utf.csv", delimiter=";")
data2 = data2.set_index(["AdmArea", "Year", "Month"])
data2 = data2.loc["Центральный административный округ"]
data2.index.names = ["Year", "Period"]
data = pd.merge(data1, data2, left_index=True, right_index=True)
data = data.reset_index()
data = data.set_index("Calls")
data = data.sort_index()
print(data["UnemployedMen"][0:1])
