s = "AAABBBCCCCXXXXXZZAAAAZZZAZAXXXCCVVVBFFFFDD"
def rle(s):
    def pack(s,cnt):
        if cnt > 1:
            return s + str(cnt)
        return s

    lastsym = s[0]
    lastpos = 0
    ans = []
    for i in range(0, len(s)):
        if s[i] != lastsym:
            ans.append(pack(lastsym, i - lastpos))
            lastpos = i
            lastsym = s[i]
    ans.append(pack(s[lastpos], len(s) - lastpos))
    return ''.join(ans)

print(rle(s))