def my_generator(n):
    for i in range(1, n+1):
        yield i

my_gen = my_generator(10)

for el in my_gen:
    print(el)