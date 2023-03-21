# age = int(input("나이를 입력하세요 → "))
# if age < 18:
#     print("집에 갈 시간이네요!")
# else:
#     print("즐거운 시간 되세요^^")
# print("협조 감사합니다.")

#=========================================================

# import random as r
# import time

# rsp = input("가위/바위/보 중 하나를 입력하시오 → ")
# start_time = time.time()
# c_rsp = r.choice(["가위", "바위", "보"])
# print(f'컴퓨터의 가위/바위/보 → {c_rsp}')

# if rsp == c_rsp:
#     print("비겼습니다.")
# elif rsp == "가위" and c_rsp == "보":
#     print("이겼습니다.")
# elif rsp == "바위" and c_rsp == "가위":
#     print("이겼습니다.")
# elif rsp == "보" and c_rsp == "바위":
#     print("이겼습니다.")
# else:
#     print("졌습니다.")

# end_time = time.time()
# taken_time = end_time - start_time
# print(f"코드 수행 시간 : {taken_time}")

#=========================================================

## 딕셔너리 사용 ver
# import random as r
# import time

# rsp = input("가위/바위/보 중 하나를 입력하시오 → ")
# start_time = time.time()
# c_rsp = r.choice(["가위", "바위", "보"])
# print(f'컴퓨터의 가위/바위/보 → {c_rsp}')

# win_dict = {"가위":"보", "바위":"가위", "보":"바위"}

# if rsp == c_rsp:
#     print("비겼습니다.")
# elif rsp in win_dict and c_rsp == win_dict[rsp]:
#     print("이겼습니다.")
# else:
#     print("졌습니다.")

# end_time = time.time()
# taken_time = end_time - start_time
# print(f"코드 수행 시간 : {taken_time}")

#=========================================================

# sum = 0
# for i in range(1, 11, 1):
#     sum += i
#     print(i, end = '')
#     if i < 10:
#         print(end = ' + ')
#     else:
#         print(end = ' = ')
# print(sum)
# print(f"1부터 10까지의 합 = {sum}")

#=========================================================

# case_num = 1
# case_num2 = 1

# for i in range(5, 0, -1):
#     case_num *= i
# print(f"A, B, C, D, E 학생들을 순서대로 세우는 경우의 수 = {case_num}")

# for j in range(1, 6, 1):
#     case_num2 *= j
# print(f"A, B, C, D, E 학생들을 순서대로 세우는 경우의 수 = {case_num2}")

#=========================================================

# sum = 0
# for i in range(1001, 2000, 2):
#     sum += i
# print(f'1000부터 2000까지의 홀수의 합 = {sum}')

#=========================================================

# for i in range(1, 10):
#     print(f"구구단 {i}단:")
#     for j in range(1, 10):
#         print(f'{i} * {j} = {i * j}')
#     print()

#=========================================================

# import secrets as scs

# r = 0

# while True:
#     r += 1
#     for i in range(1, 4):
#         globals()['d{}'.format(i)] = scs.randbelow(7) + 1
#         #print(globals()['d{}'.format(i)])
#     if d1 == d2 == d3:
#         print(f'3개의 주사위는 모두 {d1}입니다.')
#         print(f'같은 숫자가 나오기까지 {r}번 던졌습니다.')
#         break
    
#=========================================================

# import secrets as scs

# r = 0

# while True:
#     r += 1
#     num = int(input(f"{r}회 시행중 - 컴퓨터가 생각한 숫자는? "))
#     c_num = scs.randbelow(5) + 1
#     if num == c_num:
#         print("맞혔습니다. 축하합니다.")
#         break
#     else:
#         print(f"아쉽네요. 정답은 {c_num}이었습니다.")

# print("게임을 마칩니다.")