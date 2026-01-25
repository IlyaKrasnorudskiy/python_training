with open("input.txt", "r") as file:
    text = file.readline().strip()  # Считываем первую строку и убираем пробелы/переносы

max_count = 1  # Максимальная длина искомой подстроки
current_count = 1  # Текущая длина подстроки
for i in range(1, len(text)):
    if text[i] != text[i-1]:
        current_count += 1
        if current_count > max_count:
            max_count = current_count
    else:
        current_count = 1  # Сбрасываем счетчик, если символы равны

print(max_count)
