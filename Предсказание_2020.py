import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

data = pd.read_csv(
    "https://video.ittensive.com/python-advanced/data-9753-2019-07-25.utf.csv",
    delimiter=";")
data["UDP"] = 100*data["UnemployedDisabled"]/data["UnemployedTotal"]
data_group = data.groupby("Year").filter(lambda x: x["UDP"].count() > 5)
data_group = data_group.groupby("Year").mean()
x = np.array(data_group.index).reshape(len(data_group.index), 1)
y = np.array(data_group["UDP"]).reshape(len(data_group.index), 1)
model = LinearRegression()
model.fit(x, y)
print(np.round(model.predict(np.array(2020).reshape(1, 1)), 2))
