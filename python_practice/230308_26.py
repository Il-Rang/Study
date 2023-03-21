import turtle

# ------ 1번 과제 ------
# 입력 구간
num = int(input("학번을 입력해주세요 : "))
name = input("이름을 입력해주세요 : ")
hobby = input("취미를 입력해주세요 : ")

# 출력 구간
print('-------------------------------')
print(' 순천향대학교 메타버스&게임학과')
print('-------------------------------')
print(f'1. 학번: {num}')
print(f'2. 이름: {name}')
print(f'3. 취미: {hobby}')

# ------ 2번 과제 ------
print('-------------------------------')
pi = 3.1415926535
print("%d" %pi)
print("%.1f" %pi)
print("%.2f" %pi)
print("%.3f" %pi)
print("%.4f" %pi)
print("%.5f" %pi)

# ------ 3번 과제 ------
print('-------------------------------')
# 입력 구간
name = input("받는 사람을 입력해주세요 : ")
address = input("주소를 입력해주세요 : ")
gram = int(input("무게(g)를 입력해주세요 : "))
cost = gram * 5
# 출력 구간
print('-------------------------------')
print(f'받는 사람: {name}')
print(f'주소: {address}')
print(f'배송비: {cost}원')

# ------ 4번 과제 ------
turtle.shape('turtle')

turtle.forward(30)
turtle.left(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(30)
turtle.right(90)
turtle.forward(200)
turtle.left(90)

turtle.forward(50)
turtle.left(90)
turtle.forward(170)
turtle.right(90)
turtle.forward(30)
turtle.right(90)
turtle.forward(170)
turtle.left(90)
turtle.forward(30)