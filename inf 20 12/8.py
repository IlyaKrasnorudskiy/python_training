for N in range(0, 1000000000):
    R = list(bin(N)[2::])
    if R.count("0") > R.count("1"):
        ind = R.index("0")
        R[ind] = "1"
        R = "".join(R)
    else:
        R = str(R)
        R = R[::-1]
        ind = R.index("1")
        R = list(R)
        R[ind] = "0"
        R = "".join(R)[::-1]
    R = int(str(R), 2)
    print(abs(R-N))

