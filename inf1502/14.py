for p in range(7, 60):
    for x in range(0, p):
        for y in range(0, p):
            for z in range(0, p):
                first_number = y * p ** 2 + 4 * p ** 1 + y * p ** 0
                second_number = y * p ** 2 + 6 * p ** 1 + 5 * p ** 0
                last_number = x * p ** 3 + z * p ** 2 + 2 * p ** 1 + 3 * p ** 0
                if  first_number + second_number == last_number:
                    print(x * p ** 2 + y * p ** 1 + z * p ** 0, p)