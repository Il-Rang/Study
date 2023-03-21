'''
lb = int(input("파운드(lb)를 입력하세요 : "))
c_kg = lb * 0.453592
print(f'{lb} 파운드(lb)는 {c_kg : .2f} 킬로그램(kg)입니다.')

kg = int(input("킬로그램(kg)을 입력하세요 : "))
c_lb = kg * 2.204623
print(f'{kg} 킬로그램(kg)은 {c_lb : .2f} 파운드(lb)입니다.')

top = 'top'
mid = 'mid'
bot = 'bot'
test1 = f'{top : <10}'
test2 = f'{mid : ^10}'
test3 = f'{bot : >10}'
print(test1)
print(test2)
print(test3)

a = float(input("전체 인원을 입력하세요: "))
if a > 0:
    b = float(input("해당과목의 자신의 등수를 입력하세요: "))
    if 0 < b <= a:
        c = b / a * 100
        print(f"해당과목의 내신비율: {c : .3f}%")
        if c <= 4:
            print("해당과목의 내신등급: 1")
        elif 4 < c <= 11:
            print("해당과목의 내신등급: 2")
        elif 11 < c <= 23:
            print("해당과목의 내신등급: 3")
        elif 23 < c <= 40:
            print("해당과목의 내신등급: 4")
        elif 40 < c <= 60:
            print("해당과목의 내신등급: 5")
        elif 60 < c <= 77:
            print("해당과목의 내신등급: 6")
        elif 77 < c <= 89:
            print("해당과목의 내신등급: 7")
        elif 89 < c <= 96:
            print("해당과목의 내신등급: 8")
        elif 96 < c <= 100:
            print("해당과목의 내신등급: 9")
    else:
        print("1 이상 및 전체 인원의 수 이하의 값을 입력해주세요.")
else:
    print("1 이상의 값을 입력해주세요.")

import os

print("====================평균 등급 계산기====================\n")
a = int(input("과목의 총 개수를 입력하시오 : "))

t = []
r = []

for i in range(a):
    ti, ri = map(int, input(f"{i+1}번째 과목의 시수와 등급을 입력해주세요 : ").split())
    t.append(ti)
    r.append(ri)

sum_t = sum(t)
sum_ar = sum([t[i]*r[i] for i in range(a)])

os.system('cls')
er = sum_ar / sum_t

print(f"총 시수 및 등급 : {sum_t}, {sum_ar}")
print(f"평균 학점 : {er:.2f}")

with open('re.txt', 'a') as f:
    f.write(f"{er:.2f}\n")

print("====================평균 학점 계산기====================\n")

a = int(input("과목의 총 개수를 입력하시오 : ").strip())

t = []
r = []

for i in range(a):
    ti, ri = map(int, input(f"{i+1}번째 과목의 시수와 등급을 입력해주세요 : ").split())
    t.append(ti)
    r.append(ri)

total_hours = sum(t)
total_weighted_grade = sum(ti * ri for ti, ri in zip(t, r))

print("\033[H\033[J")

average_grade = total_weighted_grade / total_hours

print(f"총 시수 및 등급 : {total_hours}, {total_weighted_grade}")
print(f"평균 학점 : {average_grade:.2f}")

with open('re.txt', 'a') as f:
    f.write(f"{average_grade:.2f}\n")
'''
import secrets
random_num = secrets.randbelow(100)
print(random_num)

