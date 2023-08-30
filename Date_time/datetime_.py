#С помощью метода datetime.strptime переведите строку 'May 25 2017 5:00AM' в формат datetime.

from datetime import datetime
date = datetime.strptime('May 25 2017 5:00AM', '%b %d %Y %I:%M%p')
print(date)

#Прибавление интервала к датам
from datetime import timedelta
start_date = '2018-01-01'
end_date = '2018-01-07'
start_date_datetime = datetime.strptime(start_date, '%Y-%m-%d')
start_date_datetime + timedelta(days=1)
print(start_date_datetime)
date_time = start_date_datetime + timedelta(days=-7, minutes=-1)
print(date_time)

#Перевод обратно в строку
str_ = date.strftime('%B %d %Y %I:%M%p')
print(str_)

# как получить первый день месяца

date.strftime('%Y-%m-01')

#перечисление дат
start_date_dt = datetime.strptime(start_date, '%Y-%m-%d')
end_date_dt = datetime.strptime(end_date, '%Y-%m-%d')

print(start_date_dt, end_date_dt)

current_dt = start_date_dt

while current_dt <= end_date_dt:
    print(current_dt.strftime('%Y-%m-%d'))

    current_dt += timedelta(days=1)

list_ = [(start_date_dt + timedelta(days=x)).strftime('%Y-%m-%d') for x in range(10)]
print(list_)


# Unixtime
# Количество секунд, прошедших с 1 января 1970 года по UTC

import time
from datetime import date
from datetime import datetime
d = date(2019, 3, 11)

unixtime = time.mktime(d.timetuple())
print(unixtime)

date = datetime.fromtimestamp(1552251600)
print(date)
