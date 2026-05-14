def A(num):
    while True:
        s = str(num)
        n = len(s)
        odd_sums = 0
        for i in range(0,n,2):
            odd_sums = int(s[i])
        if odd_sums % 2 ==1:
            return 1
        even_sums = 0
        if odd_sums % 2 == 0:
            for i in range(1,n,2):
                even_sums += int(s[i])
        if even_sums % 2 ==0 or n < 5:
            return 2
        pos = n // 2
        num = int(s[:pos]+s[pos+1:])

count_state1 = 0
for num in range(10000, 20100):
    state = A(num)
    if state == 1:
        count_state1+=1
print(count_state1)
