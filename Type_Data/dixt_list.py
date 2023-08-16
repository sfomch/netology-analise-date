my_dict = {'a': {'s': {'d': {'f': 'g'}}}}
m = 5
my_list_new = []

for t in range(m):
    for l, s in my_dict.items():
        if type(s) == dict:
         my_dict = s.copy()
         my_list_new += l
my_list_new += my_dict.keys()
my_list_new += my_dict.values()
print (my_list_new)