def is_lucky_ticket(ticket_number):
    if len(ticket_number) % 2 != 0:
        raise ValueError("Количество цифр в номере билета должно быть четным")

    half_length = len(ticket_number) // 2
    first_half = sum(map(int, ticket_number[:half_length]))
    second_half = sum(map(int, ticket_number[half_length:]))

    return first_half == second_half

try:
    ticket_number = input("Введите номер билета (количество цифр должно быть четным): ")
    if is_lucky_ticket(ticket_number):
        print("Билет с номером", ticket_number, "является счастливым!")
    else:
        print("Билет с номером", ticket_number, "не является счастливым.")
except ValueError as e:
    print(e)
