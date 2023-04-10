weekdays_tuple = ('Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье')

weekends = int(input("Сколько выходных дней на неделе вы хотите? "))

if 0 <= weekends <= len(weekdays_tuple):
    working_days = weekdays_tuple[:-weekends]
    weekend_days = weekdays_tuple[-weekends:]

    print("Ваши выходные дни:", ', '.join(weekend_days))
    print("Ваши рабочие дни:", ', '.join(working_days))
else:
    print("Некорректное количество выходных дней.")
