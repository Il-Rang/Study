'''
num1 = int(input("나눠지는 수 → "))
num2 = int(input("나누는 수 → "))

result1 = num1 // num2
result2 = num1 % num2

print(f'{num1}을(를) {num2}(으)로 나눈 몫은 {result1}입니다.')
print(f'{num1}을(를) {num2}(으)로 나눈 나머지는 {result2}입니다.')

lb = int(input("파운드(lb)를 입력하세요 : "))
c_kg = round(lb * 0.453592, 5)
print(f'{lb} 파운드(lb)는 {c_kg} 킬로그램(kg)입니다.')

kg = int(input("킬로그램(kg)을 입력하세요 : "))
c_lb = kg * 2.204623
print(f'{kg} 킬로그램(kg)은 {c_lb : .3f} 파운드(lb)입니다.')
'''
money = 0
items = {'캔커피' : {'buy' : 500, 'sell' : 1800}, 
    '삼각김밥' : {'buy' : 900, 'sell' : 1400}, 
    '바나나우유' : {'buy' : 800, 'sell' : 1800}, 
    '도시락' : {'buy' : 3500, 'sell' : 4000}, 
    '콜라' : {'buy' : 700, 'sell' : 1500}, 
    '새우깡' : {'buy' : 1000, 'sell' : 2000}}

for item, price in items.items():
    buy_count = int(input(f"{item}의 구매 개수를 입력해주세요 : "))
    sell_count = int(input(f"{item}의 판매 개수를 입력해주세요 : "))
    money += (sell_count * price['sell']) - (buy_count * price['buy'])
print(f"매출액 : {money}")