'''
import random
rsp = random.randrange(1, 4)
if rsp == 1:
    print(rsp)
    print('가위')
elif rsp == 2:
    print(rsp)
    print('바위')
else:
    print(rsp)
    print('보')

#=================

score = int(input('필기 시험 점수를 입력하시오 : '))
print(score >= 70)

python = 3
mobile = 2
excel = 1

B = 3.5
A0 = 4.0
A = 4.5

avg = (python * B + mobile * A0 + excel * A) / (python + mobile + excel)
print(f'평균 학점 : {avg : .2f}')
    
#=================

cnt = 0
while 1:
    cnt += 1
    print(f"SCV {cnt}번째 미네랄을 채취 했습니다.")
    if cnt >= 10000:
        break
'''