a = []
b = [1,2,3,4,5]
c = ['life', 'is', 'too', 'short']
d = [1, 2, 'life', 'is']
e = [1, 2, [1, 2, 'life', 'is']] #이중 리스트

# print(e[0])
# print(e[1])
# print(e[2])
# print(e[2][1])
# print(e[-1][1])

print(e[:])
print(e[1:3])
print(e[1:3][1][3])