
"""

1. Какое среднее значение вызовов пожарных машин в месяц в одном округе Москвы
в 2015-2019 годах с точностью до целых?

"""


import pandas as pd

file_calls_fire = (
    'https://video.ittensive.com/python-advanced/data-5283-2019'
    '-10-04.utf.csv')

n_m1 = ['ID', 'AdmArea', 'Год', 'global_id', 'Месяц', 'Calls', 'Unnamed: 6']

#  считываем данные
data_calls_fire = pd.read_csv(
    file_calls_fire, na_values="NA", delimiter=';', names=n_m1, skiprows=1)

# заполняем 0 все не заполненное
data_calls_fire.fillna(0, axis=1, inplace=True)

# Считаем среднее кол-во вызовов
mean_calls = int(data_calls_fire.Calls.mean())
mess = (
    'Cреднее значение вызовов пожарных машин в месяц в одном округе '
    f'Москвы в 2015-2019 годах: {mean_calls}')
print(mess)
