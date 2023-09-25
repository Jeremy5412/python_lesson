# -*- coding: utf-8 -*-
burgers = ['불고기버거', '새우버거', '치즈버거', '무채소 버거']
drinks = ['스프라이트', '환타', '콜라', '민트초코 리스테린']
orderList = {} #장바구니
totalPrice = 0
priceList = {'불고기버거':3000, '새우버거': 3000, '치즈버거': 3000, '무채소 버거': 2000, '스프라이트': 100, '환타': 200, '콜라': 200, '민트초코 리스테린': 100000000, '치즈스틱': 0}

# 함수 정의 영역

def order(mtype, menu):
	if menu in mtype:
		num = int(input('메뉴 수량: '))
		if menu in orderList.keys():
			orderList[menu] += num #장바구니에 있는데 추가한 것
		else:
			orderList[menu] = num #빈 장바구니에(또는 없는 메뉴를) 새로 추가하는 것
		print('현재 주문 상태: ', orderList)
		print('{}을 추가되었습니다.'.format(menu))
	else:
		print('없음')

def pay():
	global totalPrice
	print('주문내역: ', orderList)

	for mymenu in orderList.keys():
		totalPrice += priceList[mymenu]*orderList[mymenu]

	discount = setMenu()*500
	totalPrice -= discount
	print("세트메뉴 할인 금액: {}".format(discount))
	print('총 금액: {}원'.format(totalPrice))

	if totalPrice >= 15000:
		print('치즈스틱을 드립니다')
		orderList['치즈스틱'] = 1
		print('주문내역:', orderList)

def setMenu():
	burgurcnt = 0
	drinkcnt = 0

	for myMenu in orderList.keys():
		if myMenu in burgers:
			burgurcnt += orderList[myMenu]
		elif myMenu in drinks:
			drinkcnt += orderList[myMenu]

	if burgurcnt >= drinkcnt:
		return drinkcnt
	else:
		return burgurcnt

def cancelorder():
	print('기존주문내역: ', orderList)
	cMenu = input('취소할 메뉴를 입력하세요: ')
	if cMenu in orderList.keys():
		cNum = int(input("취소할 수량을 입력하세요: "))

		if orderList[cMenu] > cNum:
			orderList[cMenu] -= cNum
			print("{}메뉴가 {}개 취소되었습니다".format(cMenu, cNum))

		elif orderList[cMenu] == cNum:
			del orderList[cMenu]
			print("선택하신 메뉴가 전체 취소되었습니다.")

		else:
			print("주문 수량보다 취소 수량이 많습니다. 다시 확인하세요.")

	else:
		print("주문내역에 없습니다. 다시 확인해주세요")


# def orderBuger(menu):
# 	if menu in burgers:
# 		orderList.append(menu)
# 		print('{}을 추가되었습니다.' .format(menu))
# 	else:
# 		print('응 없어')
# 	print('현재 주문 상태: ', orderList)
#
# def orderDrink(menu):
# 	if menu in drinks:
# 		orderList.append(menu)
# 		print('{}을 추가되었습니다.' .format(menu))
# 	else:
# 		print('응 없어')
# 	print('현재 주문 상태: ', orderList)


# 실행 영역
print('D.Burger 셀프 주문 시스템입니다.')
while True:
	orderType = int(input('메뉴 타입을 번호로 입력하세요 (버거:1/음료:2/종료:3): '))
	if orderType == 1:
		print('버거종류: ', burgers)
		mybuger = input('버거 메뉴를 입력하세요: ')
		order(burgers ,mybuger)
	elif orderType == 2:
		print('음료종류: ', drinks)
		mydrink = input('음료수 메뉴를 입력하세요: ')
		order(drinks ,mydrink)
	elif orderType == 3:
		print('-'*30)
		print("주문이 완료되었습니다.")
		print("주문 내역과 총 금액을 확인해주세요.")
		pay()

		cancel = input('주문내역수정: y / 주문완료: n: ')
		if cancel == 'y' or cancel == 'Y':
			cancelorder()
			print('주문내역과 총 금액을 확인해주세요.')
			pay()
		break