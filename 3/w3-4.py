#형(type) 변환(conversion)

a,b,c,d, = 1,'1',[1],(1,)
print(type(a),type(b),type(c),type(d))

b = int(b)
print(b, type(b))

A = int(input("숫자를 입력하세요: "))
print(A, type(A))