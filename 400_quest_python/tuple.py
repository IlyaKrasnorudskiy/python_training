tuple_in_mas = [(1, 'New-York', 'Солнечно', 5000),
                (2, 'Moscow', 'Пасмурно', 2450),
                (3, 'Chernynka', 'Солнечно', 1000),
                (4, 'Tambov', 'Дождливо', 2000),
                (5, 'Belgorod', 'Солнечно', 3221),
                (6, 'Saint-Petersburg', 'Пасмурно', 2000),
                ]
def max_amount(mas):
    max_spend_amount = 0
    for amount in mas:
        if amount[3] > max_spend_amount:
            max_spend_amount = amount[3]
    return max_spend_amount

def count_sundays(mas):
    count = 0
    for info_weather in mas:
        if info_weather[2] == 'Солнечно':
            count += 1
    return count

def info_city(mas):
    all_city = set()
    for city in mas:
        all_city.add(city[1])
    return all_city

def result(mas):
    return f"Наибольшая потраченная сумма денег: {max_amount(mas)}, Количество дней, когда была солнечная погода: {count_sundays(mas)}\n\"" \
           f"Уникальные города, которые были посещены: {info_city(mas)}"

print(result(tuple_in_mas))
