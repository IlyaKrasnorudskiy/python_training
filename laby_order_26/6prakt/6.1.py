countries_and_capitals = {
    'Россия': 'Москва',
    'Германия': 'Берлин',
    'Франция': 'Париж',
    'Италия': 'Рим',
    'Испания': 'Мадрид',
    'Великобритания': 'Лондон',
    'Китай': 'Пекин',
    'Япония': 'Токио',
    'Канада': 'Оттава',
    'США': 'Вашингтон'
}

# a)
print("Перечень стран и их столиц:")
for country, capital in countries_and_capitals.items():
    print(f"{country}: {capital}")

# b)
specific_country = 'Франция'
capital_of_specific_country = countries_and_capitals.get(specific_country)
print(f"Столица {specific_country}: {capital_of_specific_country}")

# c)
sorted_countries_and_capitals = dict(sorted(countries_and_capitals.items()))

print("Отсортированный перечень стран и их столиц:")
for country, capital in sorted_countries_and_capitals.items():
    print(f"{country}: {capital}")
