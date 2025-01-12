s = [3,45,12,124,5,-3,2,-54,53,0]
mins = -1
for i in range(len(s)):
    if s[i]%2==0 and s[i] < mins:
        mins = s[i]
print(mins)
