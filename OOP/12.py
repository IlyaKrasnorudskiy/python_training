import math
class Counter:
    def __init__(self):
        self.__counter = 0

    def __call__(self, step = 1, *args, **kwargs):
        print("__call__")
        self.__counter += step
        return self.__counter

c = Counter()
c2 = Counter()
print(c.__dict__)
c(1)
c(2)
c()
res = c()
print(res)
res2 = c2(-4)
print(res, res2)

class StripChars:
    def __init__(self, chars):
        self.__counter = 0
        self.__chars = chars

    def __call__(self, *args, **kwargs):
        if not isinstance(args[0], str):
            raise TypeError("Аргумент должен быть строкой")
        return args[0].strip(self.__chars)

s1 = StripChars("?:!,; ")
s2 = StripChars(" ")
res = s1(" ; Hello World??!  ")
print(res)
res2 = s2(" Hello World ", sep = "\n")
print(res2)

class Derivate:
    def __init__(self, func):
        self.__fn = func

    def __call__(self, x, dx= 0.0001, *args, **kwargs):
        return (self.__fn(x+dx) - self.__fn(x))/dx

@Derivate
def df_sin(x):
    return math.sin(x)

#df_sin = Derivate(df_sin)

print(df_sin(math.pi/3))