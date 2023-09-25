a = [1,2,3]
b = [4,5,6]

print(a+b)

a.extend(b)
print(a)
print(b)

print(b*10) #b 변수가 10번 반복된다.

print(len(a))
print(a[2]+4)

print(a)
a[3] = 7
a[5] = 10
print(a)
del a[4]
print(a)