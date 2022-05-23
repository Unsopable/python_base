def multi():
    return [lambda x: i*x for i in range(4)]

print([m(3) for m in multi()])


