
days_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

day, month, year, start_day = map(int, input().split())

leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

if leap:
    days_month[1] = 29

days_passed = sum(days_month[:month-1]) + (day-1)

res = (start_day - 1 + days_passed) % 7 + 1
print(res)