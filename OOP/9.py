class Person:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old

    #def get_old(self):
        #return self.__old

    #def set_old(self, old):
        #self.__old = old

    #old = property(get_old, set_old)
    @property
    def old(self):
        return self.__old
    @old.setter
    def old (self, old):
        self.__old = old

    @old.deleter
    def old(self):
        del self.__old

p = Person('Михаил', 20)
p.old = 2
print(p.__dict__)
print(p.old)
print(p.__dict__)
a = p.old
print(a)
del p.old
print(p.__dict__)