def robot(N):
    directions = [
        (0, -1),
        (-1, 0),
        (0, 1),
        (1, 0),
    ]
    x, y = 0, 0
    step = 1
    index = 0
    while N > 0:
        move_len = min(step, N)
        dx, dy = directions[index%4]
        x += dx * move_len
        y += dy * move_len
        N -= move_len
        step += 1
        index += 1
    print(x, y)
print(robot(40))