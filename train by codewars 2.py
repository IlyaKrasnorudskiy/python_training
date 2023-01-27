def increment_string(strng):
    if strng == "":
        strng = "1"
        return strng
    arr = []
    for i in range(0, len(strng)):
        if strng[i].isalpha():
            continue
        else:
            arr += strng[i]
    if len(arr) == 2:
        buf = str(int(arr[-1])+1)
        arr[-1] = buf
        strng = strng[:-2:]
        strng += "".join(arr)
        return strng
    if len(arr) == 3:

        buf = str(int(arr[-1])+1)
        arr[-1] = buf
        strng = strng[:-3:]
        strng += "".join(arr)
        return strng

print(increment_string("aaaa77"))
print(increment_string("aaaa099"))

def zeros(n):
    count = 0
    i = 5
    while (n / i>= 1):
      count += int(n / i)
      i *= 5
    return int(count)


print(zeros(300000))


def disemvowel(string_):
    l = ["I", "i", "e", "E", "a", "A", "U", "u", "O", "o"]
    for i in string_:
        if i in l:
            string_ = string_.replace(i, '')
    return string_


print(disemvowel('%ppopi[aayL"IeIe]yo|UE#ZeeuS=i~aui[@.o'))

def series_sum(n):
    start = 1
    step = 4
    for i in range(1, n):
        if i == 1:
            start += 1/step
            continue
        start += 1 / (step+3)
    return str(round(start,2))
print(series_sum(4))
