matrix = [[1,2,3],[4,5,6],[7,8,9]]

print(matrix[::-1])
a = zip(*matrix[::-1])
for b in a:
    print(b)
