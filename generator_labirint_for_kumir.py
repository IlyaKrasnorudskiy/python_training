import random

w, h = 21, 17
start = (4, 4)
goal = (19, 15)

grid = [[0 for _ in range(w)] for _ in range(h)]

for x in range(w):
    grid[0][x] = 1
    grid[h - 1][x] = 1
for y in range(h):
    grid[y][0] = 1
    grid[y][w - 1] = 1

# vertical walls
v_walls = [
    (2, 1, 6), (5, 2, 7), (8, 1, 8), (11, 3, 6),
    (14, 1, 8), (17, 2, 7)
]

# horizontal walls
h_walls = [
    (1, 2, 6), (7, 5, 7), (3, 8, 9), (10, 11, 8),
    (2, 14, 10)
]

# add walls with a single random passage in each wall
for x, y, length in v_walls:
    gap = random.randint(0, length - 1)
    for i in range(length):
        if i != gap and 0 <= x < w and 0 <= y + i < h:
            grid[y + i][x] = 1

for x, y, length in h_walls:
    gap = random.randint(0, length - 1)
    for i in range(length):
        if i != gap and 0 <= x + i < w and 0 <= y < h:
            grid[y][x + i] = 1

# add some extra internal blocks for complexity
extra = [
    (3,3),(4,3),(6,3),(7,3),
    (9,6),(10,6),(12,6),
    (5,9),(6,9),(7,9),
    (13,12),(14,12),(15,12),
]
for x, y in extra:
    grid[y][x] = 1

# carve a path by ensuring some cells are open
path = [
    (4,4),(5,4),(6,4),(7,4),(8,4),(9,4),
    (9,5),(9,6),(9,7),(10,7),(11,7),(12,7),
    (12,8),(12,9),(13,9),(14,9),(15,9),
    (15,10),(15,11),(16,11),(17,11),(18,11),(19,11),
    (19,12),(19,13),(19,14),(19,15)
]
for x, y in path:
    grid[y][x] = 0

grid[start[1]][start[0]] = 0
grid[goal[1]][goal[0]] = 0

lines = []
lines.append('; Field Size: x, y')
lines.append(f'{w} {h}')
lines.append('; Robot position: x, y')
lines.append(f'{start[0]} {start[1]}')
lines.append('; A set of special Fields: x, y, Wall, Color, Radiation, Temperature, Symbol, Symbol1, Point')

for y in range(h):
    for x in range(w):
        if grid[y][x] == 1:
            lines.append(f'{x} {y} 1 0 0.000000 0.000000 $ $ ')
        elif (x, y) == start:
            lines.append(f'{x} {y} 0 0 0.000000 0.000000 А $ ')
        elif (x, y) == goal:
            lines.append(f'{x} {y} 0 1 0.000000 0.000000 $ Б 1')

lines.append('; End Of File')

print('\n'.join(lines))