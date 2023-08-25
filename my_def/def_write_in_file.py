# Упражнение
# Напишите функцию, которая фильтрует файл visit_log.csv по источнику context и пишет результат в visits_context.csv.
# Используйте функцию из второго упражнения для проверки результата.
def write_file (file_name):
    f_visit = open(file_name, 'r')
    f_content = open('data/visit_content.csv', 'w')
    for line in f_visit:
        if 'context' in line:
            f_content.write(line)
    f_visit.close()
    f_content.close()
    return
write_file('data/visit_log.csv')