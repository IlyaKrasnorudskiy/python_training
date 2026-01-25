from itertools import product
count = 0
arr = []

for code in product(sorted("КРОВАТЬ"), repeat = 5):
    count += 1
    code = ''.join(code)
    if count % 2 != 0 and (code.count("Т") <= 1) and (code.count("В")) == 2 and ("ЬЬ" not in code):
        arr.append(count)
print(max(arr))