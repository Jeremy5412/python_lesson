t=(1,2,'a','b','c',3)
t2=[1,2,'a','b','c',3]
print(type(t))

print(t[1], t2[1])
t2[1]=5

t3=(1,3,5)
print(t+t3)

print(t3*2)

#튜플은 수정이나 삭제가 안 되지만 덧셈이나 곱셈은 가능한 리스트 하위호환 기능 (데이터 저장)

