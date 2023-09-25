age = int(input("나이?: "))
card_money = 9000

if age >= 7 and age <=12:
    print("650원 입니다.")
    print(card_money - 650)

elif age >= 13 and age <= 18:
    print("1050원 입니다.")
    print(card_money - 1050)

elif age >= 19:
    print('1250원 입니다')
    print(card_money - 1250)

