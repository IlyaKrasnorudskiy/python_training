data = [3,2,4,1]
data.sort()
if len(data) % 2 == 0:
    a = len(data)//2
    b = a - 1
    med = (data[a] + data[b])/2
else:
    a = (len(data)//2)
    med = data[a]
print(med)