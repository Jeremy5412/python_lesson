lux = {'health':490, 'mana':334, 'melee':550, 'armor':18.72}

print(lux['health'])
lux['armor']=20.50 #딕셔너리 데이터 수정
print(lux)

lux['attack_spd']=70 #딕셔너리 데이터 추가
print(lux)

del lux['melee'] #딕셔너리 데이터 삭제
print(lux)

print('health'in lux) # 키 있나
print('melee'in lux) #키 없나
print(len(lux)) #키 개수