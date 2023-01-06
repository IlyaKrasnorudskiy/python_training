def line_len(line):
    line = list(line.split())
    for i in range(len(line)):
        line[i] += str(len(line[i]))
    line = "".join(line)
    return line
print(line_len("Cегодня хорошая погода"))
