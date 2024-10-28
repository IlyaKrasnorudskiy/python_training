import time
def countingSort(inputArray):
    start_time = time.time()
    # Находим максимальный элемент в inputArray
    maxElement = max(inputArray)

    countArrayLength = maxElement + 1

    # Инициализируем countArray с (max+1) нулями
    countArray = [0] * countArrayLength

    # Шаг 1 -> Обходим inputArray и увеличиваем
    # соответствующий счётчик для каждого элемента на 1
    for el in inputArray:
        countArray[el] += 1

    # Шаг 2 -> Для каждого элемента в countArray
    # складываем его значение с значением предыдущего
    # элемента, после чего сохраняем это значение
    # как значение текущего элемента
    for i in range(1, countArrayLength):
        countArray[i] += countArray[i - 1]

    # Шаг 3 -> Вычисляем позицию элемента
    # на основе значений countArray
    outputArray = [0] * len(inputArray)
    i = len(inputArray) - 1
    while i >= 0:
        currentEl = inputArray[i]
        countArray[currentEl] -= 1
        newPosition = countArray[currentEl]
        outputArray[newPosition] = currentEl
        i -= 1

    end_time = time.time()
    execute_time = end_time - start_time
    return outputArray, execute_time

inputArray = [-4, 1000000, 5, 4, 3, -1000000]
print("Исходный массив = ", inputArray)

sortedArray = countingSort(inputArray)
print("Результат сортировки подсчётом = ", sortedArray)