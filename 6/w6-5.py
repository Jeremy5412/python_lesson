a = [24, 35, 33, 45]

for i,v in enumerate(a):
    print("index:{}, value:{}.".format(i,v))

k = 0
for b in a:
    if k < len(a):
        print("index:{}, value:{}".format(k,b))
        k += 1

for i in range(len(a)):
    print("index:{}, value:{}".format(i,a[i]))