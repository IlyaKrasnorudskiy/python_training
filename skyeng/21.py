with open("data.txt", "r") as file:  # Автоматическое закрытие файла
    data = [line.strip() for line in file]  # Чтение с удалением пробельных символов

a, b = map(int, data[0].split())  # Первая строка - два числа
total_sum = 0
count = 0

# Обрабатываем строки начиная со второй (индекс 1)
for line in data[1:]:
    if not line:  # Пропускаем пустые строки
        continue

    num = int(line)

    # Проверяем оба условия ПЕРЕД добавлением
    if num <= 100 and (total_sum + num) <= a:
        total_sum += num
        count += 1

print(count)
