i = 0
j = []
# while True:
#     i += 1
#     if i % 3 == 4:
#         j.append(i)
#     if len(j) > 20:
#         break
#
# print(j)

while True:
    i += 1
    if i % 2 == 0:
        continue
    else:
        j.append(i)

    if len(j) > 10:
        break
print(j)