import csv
import random as random


def select_sorted_func(sort_cols='high', order='asc', limit=10, filename='dump.csv'):

    '''функция сортировки'''

    def quicksort(lst):
        if len(lst) <= 1:
            return lst
        else:
            q = random.choice(lst)
            s_nums = []
            m_nums = []
            e_nums = []
            for i in range(len(lst)):
                if lst[i][sort_cols] < q[sort_cols]:
                    s_nums.append(lst[i])
                elif lst[i][sort_cols] > q[sort_cols]:
                    m_nums.append(lst[i])
                else:
                    e_nums.append(lst[i])

            return quicksort(s_nums) + e_nums + quicksort(m_nums)


    # чтение из файла
    with open('all_stocks_5yr.csv', "r") as f:
        reader = list(csv.DictReader(f))

    sort = quicksort(reader)

    # запись в файл
    with open(filename, "w") as file:
        file.write('date,open,high,low,close,volume,Name\n')
        for i in range(int(limit)):
            file.write(f'{sort[i]["date"]},{sort[i]["open"]},{sort[i]["high"]},{sort[i]["low"]},{sort[i]["close"]},'
                       f'{sort[i]["volume"]},{sort[i]["Name"]}\n')

    return sort


select_sorted_func(sort_cols='volume', order='asc', limit=20, filename='dump.csv')