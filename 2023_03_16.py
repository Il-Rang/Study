
'''
import turtle as t

t.shape("turtle")
t.up()

for i in range(10) :
    x = int(input("X 좌표 → "))
    y = int(input("Y 좌표 → "))
    text = input("쓰고 싶은 글자 → ")

    t.goto(x, y)
    t.write(text, font=("Arial", 30))

t.done()
#print(r.randrange(0, 2))
#print(r.randint(0, 2))
    
#=================

import turtle as t
import random as r

str = []
rp = int(input("몇 개의 문자열을 입력하시겠습니까? : "))
for i in range(rp):
    str.append(input(f"{i}번 인덱스에 저장될 문자열을 입력하시오 : "))
t.up()

w_rp = int(input("문자열 작성을 몇 번 반복하시겠습니까? : "))

for i in range(w_rp):
    rand_x = r.randint(-300, 300)
    rand_y = r.randint(-300, 300)
    rand_str = r.randint(0, len(str) - 1)

    t.goto(rand_x, rand_y)
    t.write(str[rand_str], font=("Arial", 30))

t.done()
    
#=================

num = int(input("정수를 하나 입력하시오 : "))
if num < 100 :
    print(f"{num}는(은) 100보다 작습니다.")
elif num == 100 :
    print(f"{num}은 100입니다.")    
else:
    print(f"{num}는(은) 100보다 큽니다.")
    
#=================

num = int(input("숫자를 입력 : "))
if num >= 100:
    if num < 1000:
        print(f"{num}은 100이상 1000미만")
    else:
        print(f"{num}은 1000이상")
else:
    print(f"{num}은 100 미만")
'''
score = int(input("해당과목의 자신의 점수를 입력하세요 : "))
if score >= 90:
    print("A", end ='')
elif score >= 80:
    print("B", end ='')
elif score >= 70:
    print("C", end ='')
elif score >= 60:
    print("D", end ='')
else:
    print("F", end ='')
print("학점입니다.")