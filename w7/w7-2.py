#함수 (사용자 정의 함수)

def hello(name):
    print('hello,', name)

def Add(a,b):
    return(a+b)

def calc(x,y):
    return x+y, x-y, x*y, x/y, x%y  #아무 자료형이나 가능하다. 결과도 그 자료형이다.

print(calc(1,2))

print(Add(1,3)) #return은 값을 반환한다.

# name = input('name: ')
# hello(name) #()=매개 변수

