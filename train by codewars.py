def multiply(a, b):
    return a * b

def boolean_to_string(b):
    return str(b)

def summation(num):
    sum = 0
    for i in range(1, num+1):
        sum+=i
    return sum


def minimum(arr):
    arr.sort()
    return arr[0]
def maximum(arr):
    arr.sort()
    return arr[-1]

