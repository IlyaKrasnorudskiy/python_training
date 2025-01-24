n = [5, 5,421,42154,2122,-211,240,40,0,442,-555,-42,102,54,123,-3]
def counting_sort(n):
    max_value = max(n)
    min_value = min(n)
    k = max_value - min_value+1
    count_arr = [0] * k

    for number in n:
        count_arr[number - min_value] += 1

    sorted_arr = []
    for i in range(0, len(count_arr)):
        if count_arr[i] == 1 and count_arr[i] != 0:
            sorted_arr.append(i + min_value)
        else:
            for j in range(0, count_arr[i]):
                sorted_arr.append(i + min_value)
    return  sorted_arr
print(counting_sort(n))