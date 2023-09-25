#리스트에 요소 추가1 append()
dlab = []
dlab.append('동탄')
dlab.append('목동')
print(dlab)

#리스트에 요소 추가2 insert()
dlab.insert(0, '판교')
print(dlab)

#정렬 함수 - sort(), reverse()
n = [1,4,3,2,5,7,6,8,9,0]
n.sort()
print(n)
n.reverse()
print(n)

#index - 위치 반환
dlab = ['p','d']
print(dlab.index('d')) #몇 번째에 있는지 알림
# print(dlab.index(1))

#pop, remove 삭제
n.remove(5)
print(n)
n.pop()
print(n)

#count - 특정 요소가 몇 개인지 알려줌
a = [1,2,3,4,4,3,2,1,1,2,3,4]
print(a.count(4)) #4가 몇개인지 나옴