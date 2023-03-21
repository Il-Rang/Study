print("-------구구단 계산기-------")
num = int(input("숫자를 입력하시오 : "))
for x in range(1, 10):
    result = num * x
    print(f'{num} 곱하기 {x}는 {result}입니다.')