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