s = "Привет, как дела? Что делаешь сегодня?!"
l = []
word = ""
k = 0
for i in range(0, len(s)):
    if not s[i].isalpha() and k!=1 :
        word = word.strip()
        l.append(word)
        word = ""
        k = 1
    else:
        word += s[i]
        k += 1
print(l)
print(min(l, key = len))