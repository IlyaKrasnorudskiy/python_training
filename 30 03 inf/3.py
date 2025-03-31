for n in range(3,10000+1):    
    s = '5' + '2' * n 
    while ('72' in s) or ('522' in s) or ('2222' in s):
        s = s.replace('72', '2', 1)
        s = s.replace('522', '27', 1)
        s = s.replace('2222', '5', 1)
    if 2*s.count("2")+5*s.count("5")+7*s.count("7") == 63:
        print(n)
        break