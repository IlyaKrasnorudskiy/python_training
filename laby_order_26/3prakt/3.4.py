import random

correct_answers = 0
wrong_answers = 0

while wrong_answers < 3:
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    correct_sum = num1 + num2
    user_sum = int(input(f"{num1} + {num2} = "))

    if user_sum == correct_sum:
        print("Правильно!")
        correct_answers += 1
    else:
        print("Ответ неверный.")
        wrong_answers += 1

print(f"Игра окончена. Правильных ответов: {correct_answers}")
