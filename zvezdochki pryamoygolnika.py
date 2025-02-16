def rectangle(r, c):
    if c > 2 and r > 2:
        print("*" * c)
        for i in range(r-2):
            print("*"+" "*(c-2)+"*")
        print("*"*c)
    else:
        for i in range(r):
            print(c*"*")