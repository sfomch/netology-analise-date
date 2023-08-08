# Задание 7
#Дана переменная, в которой хранится шестизначное число (номер проездного билета). Напишите программу, которая будет
# определять, является ли данный билет "счастливым". Билет считается счастливым, если сумма первых трех цифр совпадает
# с суммой последних трех цифр номера.
numbers_ticket = input('Введите номер билета:')
numbers_ticket_list = list(numbers_ticket)
if (int(numbers_ticket_list[0]) + int(numbers_ticket_list[1]) + int(numbers_ticket_list[2])) == \
        (int(numbers_ticket_list[3]) + int(numbers_ticket_list[4]) + int(numbers_ticket_list[5])):
    print('Счастливый билет')
else: print('Несчастливый билет')


