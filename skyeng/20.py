with open("data.txt", "r") as file:
    data = [line.strip() for line in file]

a, b = map(int, data[0].split())
total_sum = 0
max_weight = 0

for line in data[1:]:
    if not line:
        continue

    num = int(line)

    if num <= 100 and (total_sum + num) <= a:
        total_sum += num
        if num > max_weight:
            max_weight = num

print(max_weight)
