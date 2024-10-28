def find_min_P():
    min_P = float('inf')

    # Перебираем возможные значения оснований S
    for S in range(3, 100):  # начинаем с 3, так как S должно быть натуральным
        K = S + 6  # находятся K
        for a in range(S):  # a < S
            for b in range(S):  # b < S
                P_S = 2 * S ** 2 + a * S + b
                P_K = 2 * K + 7
                # Сравниваем
                if P_S == P_K:
                    min_P = min(min_P, P_S)

    return min_P


# Запускаем функцию
result = find_min_P()
print("Минимально возможное число P10:", result)
