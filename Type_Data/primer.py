# получить список из строки
sequence = '2 3 1 5 9 22 3 5 4 6 8 4 2'
sequence.split(' ')
# перевод строки в целое число
int('2')
# проверка четности
22 % 2 == 0

# f = open('data/visit_log.csv', 'r')
# content = f.readlines()
# print(content)
# for line in f:
#     print(line)
#     break

import json_
i = 0
with open('data/purchase_log.txt', encoding='utf-8') as f:
    for line in f:
        line = line.strip()

        dict_ = json.loads(line)
        print(dict_)

        i += 1
        if i > 5:
            break

