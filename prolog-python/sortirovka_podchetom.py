import time
def counting_sort(arr):
    start_time = time.time()
    max_value = max(arr)
    min_value = min(arr)

    counts = [0] * (max_value - min_value + 1)

    for number in arr:
        counts[number - min_value] += 1

    sorted_arr = []
    for i in range(0, len(counts)):
        if counts[i] == 1 and counts[i] != 0:
            sorted_arr.append(i + min_value)
        else:
            for j in range(0, counts[i]):
                sorted_arr.append(i + min_value)

    end_time = time.time()
    execution_time = end_time - start_time
    return sorted_arr, execution_time

arr = [-4, 1000000, 5, 4, 3, -1000000]
print(counting_sort(arr))
