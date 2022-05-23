foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4]
res1 = sorted(foo,key=lambda x:x<0)
res2 = sorted(foo,key=lambda x:x>0)
print(res1)  ###[8, 0, 4, 9, 8, 2, -5, -4, -20, -2, -4]
print(res2)  ###[-5, 0, -4, -20, -2, -4, 8, 4, 9, 8, 2]

res3 = sorted(foo,key=lambda x:(x<0,abs(x)))
print(res3)  ###[0, 2, 4, 8, 8, 9, -2, -4, -4, -5, -20]