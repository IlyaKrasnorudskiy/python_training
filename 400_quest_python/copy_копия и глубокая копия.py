import copy

#я в шоке, но это работает только на вложенных списках...

old_list = [[1, 2, 3], [4, 5, 6]]
new_list = old_list.copy()

new_list[0][2] = 10

print(old_list, new_list, "\n")
print(id(old_list), id(new_list) )


sec_old_list = [1, 2, 3, 4, 5]
second_list = copy.deepcopy(sec_old_list)
second_list[2] = 10
print(sec_old_list, second_list, "\n")

#Легкий способ для поверхностного копирования)
sp = [[1, 2, 3, 4, 5],[6, 7, 8, 9, 10]]

sp1 = sp[:]

sp1[1][0] = 101

print(sp, sp1)