def isValid(s):
    for i in range(0, len(s)):
        flag = 0
        for j in range(i + 1, len(s)):
            if (s[i] == '(' and s[j] == ')') or (s[i] == '[' and s[j] == ']') or (s[i] == '{' and s[j] == '}'):
                flag = 1
        if flag == 0:
            return 0
        else:
            return 1

print(isValid('{[]}'))