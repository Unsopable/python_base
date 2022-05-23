def generator():
    yield from [1,2,3,4]
a = generator()
print(type(a))  ###<class 'generator'>
print(next(a)) ## 1
print(a.__next__()) ## 2