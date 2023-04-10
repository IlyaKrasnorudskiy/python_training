while True:
    word = input("Введите слово (или введите 'stop' для завершения): ")

    if word.lower() == 'stop':
        break

    if 'ф' in word.lower():
        print("Ого! Это редкое слово!")
    else:
        print("Эх, это не очень редкое слово...")
