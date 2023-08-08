# Задание 1. Даны 2 строки: long_phrase и short_phrase. Напишите код, который проверяет действительно ли длинная фраза
# long_phrase длиннее короткой short_phrase. И выводит True или False в зависимости от результата сравнения
long_phrase = 'Насколько проще было бы писать программы, если бы не заказчики'
short_phrase = '640Кб должно хватить для любых задач. Билл Гейтс (по легенде)'
len_long = len(long_phrase)
len_short = len(short_phrase)
print("len_short = ", len_short, "len_long = ", len_long)
if len_long > len_short:
    result = True
else:
    result = False
print(result)