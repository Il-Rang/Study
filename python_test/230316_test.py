'''
import turtle as t
import secrets

str = []
rp = int(input("몇 개의 문자열을 입력하시겠습니까? : "))
for i in range(rp):
    str.append(input(f"{i}번 인덱스에 저장될 문자열을 입력하시오 : "))
t.up()

w_rp = int(input("문자열 작성을 몇 번 반복하시겠습니까? : "))

for i in range(w_rp):
    rand_x = secrets.randbelow(601) - 300
    rand_y = secrets.randbelow(601) - 300
    rand_str = secrets.randbelow(len(str))

    t.goto(rand_x, rand_y)
    t.write(str[rand_str], font=("Arial", 30))

t.done()
'''
import secrets
import time

sum = 0

rn = int(input("시행 횟수를 입력하시오 : "))
per = int(input("확률을 입력하시오 : "))

start_time = time.time()

for j in range(rn):
    r_count = 1

    while True:
        random_num = secrets.randbelow(100) + 1
        if per >= random_num:
            print(f"{j+1}번째 시행 횟수 : {r_count}")
            print(f"{j+1}번째 시행 종료")
            sum += r_count
            break
        else:
            r_count += 1
        
result = sum / rn

print(f"평균 시행 횟수 : {result:.2f}")
print(f"결과 기반 확률 : {100 / result:.2f}%")

end_time = time.time()
taken_time = end_time - start_time
print(f'수행 시간 : {taken_time}')