import csv
from turtle import pd
import pandas as pd


# def cache(func):
#     '''декоратор кеширования'''
#     cache = {}
#     def inner(arg):
#         if arg in cache:
#             return cache[arg]
#         else:
#             cache[arg] = func(arg)
#             return cache[arg]
#     print(cache)
#     return inner
#
#
# @cache
def select_sorted(sort_cols=['high'], order='asc', limit=10, filename='dump.csv'):
    '''функция сортировки'''
    sort_cols = sort_cols[0] # извлекаем параметр сортировки

    # чтение из файла
    with open('all_stocks_5yr.csv', "r") as f:
        reader = list(csv.DictReader(f))
    df = pd.DataFrame(reader)

    # проверка, в каком порядке должен быть ответ
    if order == 'desc':
        sort_d = df.sort_values(sort_cols, ascending=False)
    else:
        sort_d = df.sort_values(sort_cols)

    a = sort_d.to_dict('records')

    # запись в файл
    with open(filename, "w") as file:
        file.write('date,open,high,low,close,volume,Name\n')
        for i in range(limit):
            file.write(f'{a[i]["date"]},{a[i]["open"]},{a[i]["high"]},{a[i]["low"]},{a[i]["close"]},'
                       f'{a[i]["volume"]},{a[i]["Name"]}\n')

    return sort_d


def get_by_date(date="2017-08-08", name="PCLN", filename='dump.csv'):
    with open('dump.csv', "r") as f:
        reader = list(csv.DictReader(f))

    new = []
    for i in reader:
        if i.get('Name') == name and i.get('date') == date:
            new.append(i)

    with open(filename, "w") as file:
        file.write(f'{new}')


select_sorted(sort_cols=['high'], order='desc', limit=10, filename='dump.csv')
get_by_date(date="2017-06-16", name="AMZN", filename='dump.csv')
