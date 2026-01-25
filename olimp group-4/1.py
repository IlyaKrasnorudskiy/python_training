# перестановка робота Виталия (из условия)
# верхний ряд: 1 2 3 4 5 6 7 8 9 10
# нижний ряд: 2 1 9 3 4 5 7 8 10 6
# т.е. из коробки i шарик кладётся в box_to[i]
box_to = [0, 2, 1, 9, 3, 4, 5, 7, 8, 10, 6]  # индекс 0 не используем

n = 10
k = 2026  # число запусков робота

# разложим перестановку на циклы
visited = [False] * (n + 1)
final_box_for_ball = [0] * (n + 1)  # куда попадёт шарик с данным номером

for start in range(1, n + 1):
    if not visited[start]:
        cycle = []
        v = start
        while not visited[v]:
            visited[v] = True
            cycle.append(v)
            v = box_to[v]

        m = len(cycle)
        # после k применений перестановки шарик из позиции cycle[i]
        # окажется в позиции cycle[(i + k) % m]
        shift = k % m
        for i, pos in enumerate(cycle):
            final_pos = cycle[(i + shift) % m]
            # в коробке final_pos окажется шарик, который был в pos
            final_box_for_ball[pos] = final_pos

# вывод ответа: для каждого номера шарика (1..10) номер коробки, где он окажется
result = [final_box_for_ball[i] for i in range(1, n + 1)]
print(*result)
