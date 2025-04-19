def digit_sum(n):
    num_str = str(abs(n))
    sums = 0
    for char in num_str:
        digit = int(char)
        sums += digit

    return sums


def same_digit_sum(arr):
    if len(arr) == 0:
        return True

    first_sum = digit_sum(arr[0])
    for number in arr[1:]:
        current_sum = digit_sum(number)
        if current_sum != first_sum:
            return False
    return True

