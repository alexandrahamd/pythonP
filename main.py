import csv
from turtle import pd
import pandas as pd
from distlib.compat import raw_input


# def cache(func):
#     '''декоратор кеширования'''
#     cache = {}
#     def inner(**kwargs):
#         print(kwargs)
#         args = tuple(kwargs)
#         if args in cache:
#             return cache[args]
#         else:
#             cache[args] = func(args)
#             return cache[args]
#     print(cache)
#     return inner
# def cache(f):
#     cache = {}
#     def wrapper(*args, **kwargs):
#         key = tuple(f'{f}, {args}, {kwargs}')
#         if key not in cache:
#             cache[key] = f(*args, **kwargs)
#         return cache[key]
#     return wrapper
#
# @cache
def select_sorted():
    '''функция сортировки для пользователя'''
    sort_cols = raw_input('Сортировать по цене открытия(1),закрытия(2),максимум[3],минимум(4),объем(5):') or 'high'
    if sort_cols == '1':
        sort_cols = 'open'
    elif sort_cols == '2':
        sort_cols = 'close'
    elif sort_cols == '3':
        sort_cols = 'high'
    elif sort_cols == '4':
        sort_cols = 'low'
    elif sort_cols == '5':
        sort_cols = 'volume'

    order = raw_input('Порядок по убыванию [1] / возрастанию (2): ') or 'asc'
    if order == '1':
        order = 'desc'
    elif order == '2':
        order = 'asc'

    limit = raw_input('Ограничение выборки [10]:') or '10'
    filename = raw_input('Название файла для сохранения результата [dump.csv]:') or 'dump.csv'

    return select_sorted_func(sort_cols, order, limit, filename)


# @cache
def select_sorted_func(sort_cols='high', order='asc', limit=10, filename='dump.csv'):
    '''функция сортировки'''
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
        for i in range(int(limit)):
            file.write(f'{a[i]["date"]},{a[i]["open"]},{a[i]["high"]},{a[i]["low"]},{a[i]["close"]},'
                       f'{a[i]["volume"]},{a[i]["Name"]}\n')

    return sort_d


def get_by_date():
    ''' функция выбора для клиента'''
    date = raw_input('Дата в формате yyyy-mm-dd [all]:') or 'all'
    name = raw_input('Тикер [all]:') or 'all'
    filename = raw_input('Файл [new.csv]:') or 'new.csv'

    get_by_date_func(date, name, filename)


def get_by_date_func(date="2017-08-08", name="PCLN", filename='new.csv'):
    ''' функция выбора '''
    with open('dump.csv', "r") as f:
        reader = list(csv.DictReader(f))

    new = []
    for i in reader:
        if i.get('Name') == name and i.get('date') == date:
            new.append(i)

    for i in reader:
        if date != 'all' and name != 'all' and i.get('Name') == name and i.get('date') == date:
            new.append(i)
        elif date == 'all' and name == 'all':
            new.append(i)
        elif date != 'all' and name == 'all' and i.get('date') == date:
            new.append(i)
        elif date == 'all' and name != 'all' and i.get('Name') == name:
            new.append(i)
    with open(filename, "w") as file:
        file.write(f'{new} \n')


get_by_date_func(date="2017-08-08", name="PCLN", filename='new.csv')


