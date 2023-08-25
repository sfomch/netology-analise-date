# def read_file (file_name):
#     with open(file_name, encoding='utf-8') as f:
#         five_str = list([next(f).strip() for x in f])
#     return five_str
#
# my_list = read_file('data/purchase_log.txt')
# print(my_list)
import json
# i = 0
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
with open('data/visit_log.csv', encoding='utf-8') as f_visit:
    with open('data/funnel.csv', 'a') as f_buy:
        i=0
        for key, value in dict_user.items():
            for line in f_visit:
                line = line.strip()
                i = i + 1
                print(i)
                if key in line:

                    f_buy.write(f'{line}, {value}\n')

print(shop_category)
print(dict_user)


        # i += 1
        # if i > 5:
        #     break