# sum = 0
# n1, n2 = 0, 0

# while True :
#     n1 = int(input("num1 → "))
#     n2 = int(input("num1 → "))

#     sum = n1 + n2
#     print(f'{n1} + {n2} = {sum}')

#=======================================================

# for i in range(5):
#     for j in range(5):
#         if j == 2:
#             continue
#         print(f'i = {i}, j = {j}')

#=======================================================

# sum = 0
# n1, n2 = 0, 0

# while True :
#     n1 = int(input("num1 → "))
#     if n1 == 0:
#         break
#     n2 = int(input("num1 → "))

#     sum = n1 + n2
#     print(f'{n1} + {n2} = {sum}')

# print("0을 입력해서 계산을 종료합니다.")

#=======================================================

# sum = 0
# for i in range(1, 101, 1):
#     if i % 4 == 0:
#         continue

#     sum += i

# print(f'1~100까지의 합계(4의 배수 제외) = {sum}')

#=======================================================

# import random

# wiseSay = [
# "삶이 있는 한 희망은 있다",
# "언제나 현재에 집중할 수 있다면 행복할 것이다",
# "신은 용기있는 자를 결코 버리지 않는다",
# "피할 수 없으면 즐겨라",
# "행복한 삶을 살기위해 필요한 것은 거의 없다",
# "내일은 내일의 태양이 뜬다",
# "계단을 밟아야 계단 위에 올라설 수 있다",
# "행복은 습관이다, 그것을 몸에 지니라",
# "1퍼센트의 가능성, 그것이 나의 길이다",
# "작은 기회로 부터 종종 위대한 업적이 시작된다" ]

# today = random.randint(0, len(wiseSay)-1)
# print("오늘의 명언 ==>", wiseSay[today])