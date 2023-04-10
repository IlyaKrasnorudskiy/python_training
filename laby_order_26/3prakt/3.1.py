N = int(input("Введите количество слов: "))
words = []

for i in range(N):
    word = input("Введите слово {}: ".format(i + 1))
    words.append(word)

long_string = ' '.join(words)
print("Результат: ", long_string)
