# x = 15
# if x> 10:
#     print('10보다 쿰')
#
#     if x == 15:
#         print('x는 15')
#
#     if x == 20:
#         print('x는 20')

AGE = int(input("age?"))
gen = input("성별? (m or f)")

if AGE > 19:
    print('성인입니다')
    if gen == 'm':
        print('남자입니다')
    else:
        print("여자입니다.")

else:
    print("미성년자입니다")
    if gen == 'm':
        print('남자입니다')
    else:
        print("여자입니다.")