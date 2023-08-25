# Посчитайте распределение количества покупок по категориям в столбце category
# Составьте словарь, в котором для каждого user_id значением будет название категории
# Для каждого user_id в файле visit_log.csv определите третий столбец с категорией покупки (если покупка была,
# сам файл visit_log.csv изменять не надо). Запишите в файл funnel.csv визиты из файла visit_log.csv, в которых были
# покупки с указанием категории.

import json

with open('data/purchase_log.txt', encoding='utf-8') as f:
    shop_category ={}
    dict_user = {}
    for line in f:
        line = line.strip()
        dict_ = json.loads(line)
        dict_user[dict_['user_id']] = dict_['category']
        if dict_['category'] not in shop_category and dict_['category'] !='category':
            shop_category[dict_['category']] = 1
        elif dict_['category'] !='category':
            shop_category[dict_['category']] += 1
print(shop_category)

with open('data/visit_log.csv', encoding='utf-8') as f_visit:
    with open('data/funnel.csv', 'a') as f_buy:
        for line in f_visit:
            line_1 = line.strip()[:10]
            if dict_user.get(line_1) != None:
                f_buy.write(f'{line.strip()}, {dict_user[line_1]}\n')
