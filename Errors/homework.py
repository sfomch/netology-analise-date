#Домашнее задание к лекции "Исключения и обработка ошибок"
# **Домашнее задание **
#
# Задание 1
# Напишите функцию date_range, которая возвращает список дней между датами start_date и end_date.
# Даты должны вводиться в формате YYYY-MM-DD.
#
# Задание 2
# Дополните функцию из первого задания проверкой на корректность дат.
# В случае неверного формата или если start_date > end_date должен возвращаться пустой список.
#
# Задание 3
# Дан поток дат в формате YYYY-MM-DD, в которых встречаются некорректные значения:
# stream = [‘2018-04-02’, ‘2018-02-29’, ‘2018-19-02’]
#
# Напишите функцию, которая проверяет эти даты на корректность. Т. е. для каждой даты возвращает True (дата корректна) или False (некорректная дата).
#

from datetime import datetime
from datetime import timedelta

start_date = input('Введидите начальную дату в формате YYYY-MM-DD:')
end_date = input('Введидите конечную дату в формате YYYY-MM-DD:')


def date_range (start_date, end_date):
    list_ = ''
    try:
        start_date_dt = datetime.strptime(start_date, '%Y-%m-%d')
        end_date_dt = datetime.strptime(end_date, '%Y-%m-%d')
    except:
        list_ = 'неверный формат даты'
        return list_
    if start_date_dt > end_date_dt:
        list_ = 'начальная дата больше конечной'
        return list_
    current_dt = start_date_dt
    while current_dt <= end_date_dt:
        list_ += (current_dt.strftime('%Y-%m-%d') +'\n')
        current_dt += timedelta(days=1)
    return  list_

a = date_range(start_date, end_date)
print(a)
#
#
