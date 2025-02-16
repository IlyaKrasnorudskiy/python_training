def find_left_cell(grid):
    for i in range(2):
        for j in range(2):
            if grid[i][j] == 1:

                return (i, 0)


grid = [
    [1, 0],
    [0, 0]
]

left_cell = find_left_cell(grid)
print(f"Робот должен быть в клетке: {left_cell}")
