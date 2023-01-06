def count_diff_word(line):
    m = []
    n = 0
    for i in line:
        if not i in m and i != '.':
            m += i
            n += 1
    line = "Кол-во различных букв равно: ", n
    return line


print(count_diff_word("lineline."))
