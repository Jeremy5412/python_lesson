# for i in range(5): #바깥쪽 루프
#     for j in range(5): #안쪽 루프
#         print('j: ',j, sep='', end=' ')
#
#     print('i:',i, '\\n', sep='')

# for k in range(5):
#     for i in range(5):
#         print("*", end=' ')

    # print()

for i in range(5):
    for j in range(5):
        if j <= i:
            print('ㅗ', end=' ')
    print()