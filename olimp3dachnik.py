N = int(input())
half = N // 2
max_area = 0

for a in range(1, half):
    b = half - a
    if b > 0:
        area = a * b
        if area > max_area:
            max_area = area

print(max_area//2)