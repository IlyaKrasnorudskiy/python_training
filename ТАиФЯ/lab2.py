def is_in_language(word):
    # Начальное состояние автомата
    state = 'q0'

    # Проходим по каждому символу входного слова
    for char in word:
        if state == 'q0':
            if char == '0':
                state = 'q0'
            elif char == '1':
                state = 'q1'
        elif state == 'q1':
            if char == '0':
                state = 'q2'
            elif char == '1':
                state = 'q1'
        elif state == 'q2':
            if char == '0':
                state = 'q0'
            elif char == '1':
                state = 'q1'

    # Проверяем, находится ли автомат в принимающем состоянии
    if state == 'q2':
        return True, state
    else:
        return False, state

# Тестируем автомат
word = input("Введите слово: ")
belongs, final_state = is_in_language(word)

if belongs:
    print(f"Слово принадлежит языку. Итоговое состояние: {final_state}")
else:
    print(f"Слово не принадлежит языку. Итоговое состояние: {final_state}")
