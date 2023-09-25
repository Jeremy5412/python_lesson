import random

a = random.randint(1,10)
print(a)
b = ['a','b','c','f','g']
b1 = random.choice(b)
print(b1)
c = random.sample(b,3)
print(c)

# num = int(input("종료 숫자: "))
# cnt = 0 #반복 수
# i = 0
#
# while i != num:
#     i = random.randint(1,1000000)
#     print(i)
#     cnt += 1
#
# print("{} 번 반복 했음".format(cnt))