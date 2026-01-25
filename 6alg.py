arr = []
for N in range(1, 10000):
    count_ed = 0
    count_zero=0
    R = bin(N)[2::]
    for i in range(0,len(R)):
        if (int(i)+1) % 2 == 0 and R[i] == '1':
            count_ed += 1
        elif (int(i)+1) % 2 != 0 and R[i] == '0':
            count_zero += 1
    R = abs(count_ed - count_zero)
    if R == 5:
        print(N)
        break