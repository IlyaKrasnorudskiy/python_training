n = 3
m = 2
mas_plot = [5,10,7,5,5,5]
mas_meskl = [9, 5, 3, 5, 12, 10]
pl = []
ms = []
count = 0
for i in range(0, n):
    for j in range(0, n):
        if mas_plot[i] > mas_meskl[i]:
            count += 1



print(count)