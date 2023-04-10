my_list = [1, 2, 3, 4, 5, 3, 6, 7]

repeated_elements = []

for element in my_list:
    if my_list.count(element) > 1 and element not in repeated_elements:
        repeated_elements.append(element)

if repeated_elements:
    print("Повторяющиеся элементы в списке:", repeated_elements)
else:
    print("В списке нет повторяющихся элементов.")
