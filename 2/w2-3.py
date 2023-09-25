t = "hobby"
p = "Python is the best choice."
m = "You need python."

#count()
print(t.count('b'))
print(p.find ('s'))
print(p.find('L')) #없을 때는 -1을 출력합니다

#index()
print(p.find('s'))
print(p.find('L')) #없다고 나온다.

#join()
print('/'.join(t))

#upper(), lower()
print(m.upper()) #모든 문자를 대문자로

#strip() - lstrip(), rstrip(), strip()
word = ' python '
print(word.lstrip()+ 'py') #뒷쪽 공백
print('py'+ word.rstrip()) #앞쪽 공백
print("py"+ word.strip()+ "py") #공백 없음

#replace()
oldname = 'james'
newname = 'jay'
res = '회장은 %s 입니다' %oldname
new = res.replace(oldname, newname) #res변수에서 oldname을 newname으로 바꿉니다.
print(new)

#split() #결과는 리스트로 표현
print(p.split()) #공백 기준으로 나눔 ()안에 아무것도 없을 때
r = 'Process/finish/with/exit/code'
print(r.split('/')) #/기준으로 나눔