# # 1번 과제

# num = int(input("출력할 단수를 입력하시오 : "))
# for x in range(1, 10):
#     result = num * x
#     print(f'{num} 곱하기 {x}는 {result}입니다.')

#===========================================================
# # 2번 과제

# score = int(input("점수 입력 (0~100) : "))
# if score >= 90:
#     print("A")
# elif score >= 80:
#     print("B")
# elif score >= 70:
#     print("C")
# elif score >= 60:
#     print("D")
# else:
#     print("F")

#===========================================================
# # 3번 과제

# sum = 0
# n = int(input("숫자 입력 : "))
# for i in range(1, n+1, 1):
#     sum += i
# print(f'1부터 {n}까지의 합 = {sum}')

#===========================================================
# 4번 과제

n1 = int(input("숫자 입력 : "))
n2 = int(input("배수 입력 : "))
for i in range(n2, n1+1, n2):
    print(i, end = ', ')

#===========================================================
# # 5번 과제

# import random

# for i in range(10):
#     num1to45 = list(range(1, 46, 1))
#     result = list()
#     for j in range(6):
#         rn = random.choice(num1to45)
#         result.append(rn)
#         num1to45.remove(rn)
#     print(result)  