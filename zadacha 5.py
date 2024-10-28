m = int(input())
s = int(input())
p = int(input())
q = int(input())

remaining_time = (48 * 60) - (m * 60 + s)

number_of_attacks = remaining_time // 24 / 2

final_points_warriors = p + number_of_attacks * 3
final_points_celtics = q + number_of_attacks * 2

print(int(final_points_warriors), int(final_points_celtics))
