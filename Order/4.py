line = input()
line_l_and_split = lambda line : list(line.split())
obj_first = line_l_and_split(line)
line_len = lambda obj_first: [obj_first[i] + str(len(obj_first[i])) for i in range(0, len(obj_first))]
obj_second = line_len(obj_first)
line_join = lambda obj_second: "".join(obj_second)
print(line_join(obj_second))
