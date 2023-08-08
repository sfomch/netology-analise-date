# Задание 3. Разработать приложение для определения знака зодиака по дате рождения. Пример:
birdmon = input('Введите месяц рождения в формате "месяц"')
birdday = int(input('Введите день рождения в формате "dd"'))
if (birdmon == 'январь' and birdday < 20) or (birdmon == 'декабрь' and birdday >= 22):
    print('Козерог')
elif (birdmon == 'февраль' and birdday < 19) or (birdmon == 'январь' and birdday >= 20):
    print('Водолей')
elif (birdmon == 'март' and birdday < 21) or (birdmon == 'февраль' and birdday >= 19):
    print('Рыбы')
elif (birdmon == 'апрель' and birdday < 20) or (birdmon == 'март' and birdday >=21 ):
    print('Овен')
elif (birdmon == 'май' and birdday < 21) or (birdmon == 'апрель' and birdday >= 20):
    print('Телец')
elif (birdmon == 'июнь' and birdday < 21) or (birdmon == 'май' and birdday >= 21):
    print('Близнецы')
elif (birdmon == 'июль' and birdday < 23) or (birdmon == 'июнь' and birdday >= 21):
    print('Рак')
elif (birdmon == 'август' and birdday < 23) or (birdmon == 'июль' and birdday >= 23):
    print('Лев')
elif (birdmon == 'сентябрь' and birdday < 23) or (birdmon == 'август' and birdday >= 23):
    print('Дева')
elif (birdmon == 'октябрь' and birdday < 23) or (birdmon == 'сентябрь' and birdday >= 23):
    print('Весы')
elif (birdmon == 'ноябрь' and birdday < 22) or (birdmon == 'октябрь' and birdday >= 23):
    print('Скорпион')
elif (birdmon == 'декабрь' and birdday < 22) or (birdmon == 'ноябрь' and birdday >= 22):
    print('Стрелец')
else: print("Вы неправильно ввели дату рождения")
