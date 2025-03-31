dictionary = {}
for i in range(4):
    a = str(input())
    a = a.split()
    dictionary[a[0]] = a[1]

dictionary['reading'], dictionary['writing'] = dictionary['writing'], dictionary['reading']
for key, value in dictionary.items():
    print(key, "-", value)