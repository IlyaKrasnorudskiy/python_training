mas = [1, 2, 3, 4, 5]
iterator = iter(mas)
a = next(iterator)
print(next(iterator))

def generator():
    yield 1
    yield 2
    yield 3

new_iterator = generator()
print(next(new_iterator))
print(next(new_iterator))
print(next(new_iterator))
