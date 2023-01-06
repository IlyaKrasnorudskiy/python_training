def homework(n):
    arr = {}
    for i in range(0, n):
        word = input()
        wordl = word.lower()
        if wordl not in arr:
            arr[wordl] = set()
        arr[wordl].add(word)
    errors = 0
    sentence = input().split()
    for word in sentence:
        if ((wordl in arr and wordl not in arr[wordl]) or len([up_litera for up_litera in wordl if up_litera.isupper()]) != 1):
            errors += 1
    return errors

print(homework(5))