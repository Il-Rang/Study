inst = {}
items = ['색소폰', '바이올린', '피아노', '트럼펫', '일렉기타', '베이스기타', '통기타', '리코더', '우쿨렐레', '플루트']
counts = [80, 74, 92, 52, 21, 94, 48, 64, 20, 89]
for i in range(len(items)):
    inst [f'{items[i]}'] = counts[i]
print(f'#1 : {inst}')

inst['색소폰'] = 1000
print(f'#2 : {inst}')

del inst['트럼펫']
print(f'#3 : {inst}')

sum = 0
min = 100
max = 0
for x in inst.keys():
    sum += inst[x]
print(f'#4 : {sum}')

for y in inst.keys():
    if min > inst[y]:
        min = inst[y]
        min_item = y
print(f'#5 : {min_item} {min}')

for z in inst.keys():
    if max < inst[z]:
        max = inst[z]
        max_item = z
print(f'#6 : {max_item} {max}')

import random as r
for i in range(len(items)):
    inst [f'{items[i]}'] = [counts[i], r.randint(10000, 99999)]
print(f'#7 : {inst}')

m_max = 0
m_items = 0
for q in inst.keys():
    mul = inst[q][0] * inst[q][1]
    if m_max < mul:
        m_max = mul
        m_items = q
print(f'#8 : 개수 * 가격이 가장 높은 악기명 : {m_items}')

instl = []
cntl = []
pril = []
for w in inst.keys():
    instl.append(w)
    cntl.append(inst[w][0])
    pril.append(inst[w][1])
print(f'#9 : 악기 리스트 : {instl}')
print(f'#9 : 개수 리스트 : {cntl}')
print(f'#9 : 가격 리스트 : {pril}')

# 추가 문제
iny = int(input("열 크기 입력 : "))
inx = int(input("행 크기 입력 : "))
if inx >= iny:
    xy_max = inx
else:
    xy_max = iny

for y in range(iny):
    pcnt = y
    for x in range(inx):
        pcnt += 1
        if pcnt > xy_max:
            pcnt = 1
        print(pcnt, end = ' ')
    print()