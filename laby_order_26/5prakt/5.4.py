group1 = ['Иванов', 'Петров', 'Сидоров', 'Кузнецов', 'Смирнов', 'Васильев', 'Попов', 'Соколов', 'Михайлов', 'Новиков']
group2 = ['Орлов', 'Титов', 'Комаров', 'Киселев', 'Григорьев', 'Павлов', 'Козлов', 'Степанов', 'Никонов', 'Савельев']

team1 = group1[:5]
team2 = group2[:5]

sport_team = tuple(team1 + team2)

print("Группа 1:", group1)
print("Группа 2:", group2)
print("Спортивная команда:", sport_team)
print("Длина команды:", len(sport_team))

sorted_team = tuple(sorted(sport_team))
print("Отсортированная команда:", sorted_team)

ivanov_count = sorted_team.count("Иванов")
if ivanov_count > 0:
    print("Студент 'Иванов' входит в команду и встречается", ivanov_count, "раз(а).")
else:
    print("Студент 'Иванов' не входит в команду.")
