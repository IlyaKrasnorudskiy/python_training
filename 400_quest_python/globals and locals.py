x = 1
def test_function():
    a = 10
    b = 20
    print("Локальные переменные:", locals())

test_function()
print("Глобальные переменные:", globals())
