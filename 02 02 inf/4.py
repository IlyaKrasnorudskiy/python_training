n = int(input())
students = []

for i in range(n):
    data = input().split()
    surname = data[0]
    name = data[1]
    marks = list(map(int, data[2:]))
    avg = sum(marks)/3
    students.append((surname, name, avg))



students.sort(key = lambda student: student[2], reverse = True)
top_students = []
top_score = students[0][2]
for student in students:
    if student[2] == top_score:
        top_students.append(student)
    else:
        break
for student in top_students:
    print(student)