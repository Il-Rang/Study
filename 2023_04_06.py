# def sumfunc():
#     n1 = int(input("1번째 값 : "))
#     n2 = int(input("2번째 값 : "))
#     return n1 + n2

# def sumfunc(n1, n2):
#     return n1 + n2
# sum = sumfunc(1, 5)
# print(sum)

# def calc():
#     op = input("계산 입력 (+, -, *, /) : ")
#     fn = int(input("첫 번째 숫자 입력 : "))
#     sn = int(input("두 번째 숫자 입력 : "))
#     if op == '+':
#         print(f"{fn} {op} {sn} = {fn + sn}")
#     elif op == '-':
#         print(f"{fn} {op} {sn} = {fn - sn}")
#     elif op == '*':
#         print(f"{fn} {op} {sn} = {fn * sn}")
#     elif op == '/':
#         print(f"{fn} {op} {sn} = {fn / sn}")
#     else:
#         print(f"제대로 된 값을 입력하시오.")
# calc()

# def calc(n1, n2, op):
#     if op == '+':
#         result = n1 + n2
#     elif op == '-':
#         result = n1 - n2
#     elif op == '*':
#         result = n1 * n2
#     elif op == '/':
#         result = n1 / n2
#     else:
#         print(f"제대로 된 값을 입력하시오.")
#     return result

# res = 0
# var1, var2, oper = 0, 0, ""
# oper = input("계산 입력 (+, -, * , /) : ")
# var1 = int(input("첫 번째 숫자 입력 : "))
# var2 = int(input("두 번째 숫자 입력 : "))
# res = calc(var1, var2, oper)
# print(f"{var1} {oper} {var2} = {res}")

# import random as r

# def getnum():
#     l = []
#     cnt = 0
#     while cnt < 6:
#         rn = r.randint(1, 45)
#         if rn not in l:
#             l.append(rn)
#             cnt += 1
#     return l

# lotto = getnum()
# lotto.sort()
# print(f"로또 번호 출력 : {lotto}")

import random as r

def getnum(l):
    while True:
        rn = r.randint(1, 45)
        if rn not in l:
            break
    return rn

ul = []
for i in range(6):
    ul.append(getnum(ul))

ul.sort()
print("로또 번호 출력 :", end = ' ')
for j in ul:
    print(j , end = ' ')