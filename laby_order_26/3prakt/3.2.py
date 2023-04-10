words = []

while True:
    word = input("Введите слово (или введите 'stop' для завершения): ")

    if word.lower() == 'stop':
        break

    words.append(word)

long_string = ' '.join(words)
print("Результат: ", long_string)
