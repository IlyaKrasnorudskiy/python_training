def graph(func):
    x_arr = []
    y_arr = []
    for x in range(-10,11):
        x_arr.append(x)
        a = eval(func)
        y_arr.append(a)
    print("x: ", *x_arr)
    print("y: ", *y_arr)


print(graph("2 * x - 5"))