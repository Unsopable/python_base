from inspect import isclass, ismethod


class A():
    def __init__(self,c) -> None:
        self.c = c
    def meth(self):
        print('asd')
        
a = A(323)

print(isclass(A))  ###True

print(ismethod(a.meth))   ####True