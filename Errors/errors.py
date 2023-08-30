data = ['90', '60', '90', '240tot']
total_sum = 0

for num in data:
    try:
        total_sum += float(num)

    except:
        print('Ошибка в данных: {}'.format(num))

print('Итого', total_sum)


#
# полная версия traceback
import traceback

try:
    float('123fff')

except Exception:
    print(traceback.print_exc())

print('Проехали')