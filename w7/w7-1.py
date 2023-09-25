a = [[10, 20],
     [30, 40],
     [50, 60]]

print(a[0][0])
print(a[0][1])

print(a[1][0])
print(a[1][1])

for i in a:
    for j in i:
        print(j, end=" ")
    print()

for x,y in a:
    print(x,y)