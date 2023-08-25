# Дан список произвольной длины. Необходимо написать код, который на основе исходного списка составит словарь такого
# уровня вложенности, какова длина исхондого списка.
my_list = ['a', 's', 'd', 'f', 'g']
my_dict = {}
my_dict[my_list[-2]] = my_list[-1]
n = -(len(my_list))
i = -2
while i > n:
  new_dict = my_dict.copy()
  my_dict.pop(my_list[i])
  my_dict[my_list[i-1]] = new_dict
  i = i - 1
print (my_dict)


