def duplicate_count(text):
    text = text.upper()
    print(text)
    count = 0
    for i in text:
        if text.count(i) > 1:
            count+=1
            text = text.replace(i, '')
            print(text)
    return count
print(duplicate_count('aabbcc'))
#Солидно



def unique_in_order(iterable):
    l = []
    for i in range(len(iterable)-1 ):
        buf = iterable[i]
        if buf != iterable[i+1]:
            l.append(buf)
    l.append(iterable[-1])
    return l
print(unique_in_order(('AAAABBBCCDAABB  B')))


def even_or_odd(number):
    if number % 2 == 0:
        return 'Even'
    else:
        return 'Odd'
