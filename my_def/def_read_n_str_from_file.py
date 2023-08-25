# Упражнение
# Напишите функцию (или просто код), который возвращает список из первых N строк файла purchase_log.txt без
# записи всего содержимого файла в оперативную память.
def read_file (file_name):
    f = open(file_name, 'r', encoding='utf-8')
    five_str = []
    for i in range(5):
        five_str.append(f.readline().strip())
    f.close()
    return five_str

my_list = read_file('data/purchase_log.txt')
print(my_list)

def read_file_5 (file_name):
    with open(file_name, encoding='utf-8') as f:
        five_str5 = list([next(f).strip() for x in range(5)])
    return five_str5

my_list5 = read_file_5('data/purchase_log.txt')
print(my_list5)

