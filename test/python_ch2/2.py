line = str(input())
line = line.split()
for i in range(0, len(line)):
    line[i] = int(line[i])
maxs = max(line)
line.remove(maxs)
line = map(str, line)
print(' '.join(line))
