lux = {'health':490, 'mana':334, 'melee':550, 'armor':18.72} #왼쪽 문자는 key, 오른쪽 숫자는 value. value는 key마다 한개, 복수 지정은 list로
                                             #key가 같은게 2개 있으면 뒤에있는게 표시된다.
#print(type(lux))

#X={100:'hundred', False:0, 3.5:[1,2,3]} #일반적인 딕셔너리는 key에 1대1이여야한다.
#print(X)

y = dict()
print(y)
a = dict(age=20, addr='가영만, Hongkong')
print(a)

lux_key = lux.keys()    #키의 값 확인
lux_value = lux.values()
print(lux_value)
print(lux_key)