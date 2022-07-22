#Разработать функцию count_holes (n), которая принимает 1 аргумент — целое число или строку, содержащую целое число,
#и возвращает целое число — количество «отверстий» в десятичной записи этого числа печатными цифрами
#(считать, что в «4» и в «0» по одному отверстию), или строку ERROR , если переданный аргумент не удовлетворяет требованиям:
#является действительным или вообще не числом.
def count_holes(st):
    if isinstance(st, float):
        return 'ERROR'
    try:
        dict = {"0": 1, "4": 1, "6": 1, "8": 2, "9" : 1}
        st = int(st)
        st = str(st)
        keys = list(dict.keys())
        k = 0
        for a in st:
            if a in keys:
                k += dict[a]
        return k
    except ValueError:
        return "ERROR"
    except TypeError:
        return "ERROR"
    except NameError:
        return "ERROR"

line = 889999
print(count_holes(line))

