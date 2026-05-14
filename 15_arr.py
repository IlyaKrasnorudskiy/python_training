P=[i for i in range(10,40)]
Q=[i for i in range(23,59)]
a=[]
for Amin in range(100):
    for Amax in range(Amin,100):
        A=[i for i in range(Amin,Amax)]
        z=1
        for x in range(100):
            if not((((x in P) and (x in Q)) <= ((x in Q) and (x in A)))):
                z=0
        if z==1:
            a.append(len(A))
print(min(a)-1)