cnt_index = 0
sum = 0
sum_2 = 0

nList = list(range(1, 31)) # 1 ~ 30까지의 값을 지닌 리스트를 생성
print(f"1 : {nList}")
nList[0] = 1000
print(f"2 : {nList}")
nList[-1] = 3000
print(f"3 : {nList}")
for i in range(31, 41):
    nList.append(i)
print(f"4 : {nList}")
for x in range(0, len(nList)):
    if nList[x] >= 100:
        nList[x] = x + 1
print(f"5 : {nList}")

print(f"6 : {nList[0 : 6]}")
print(f"7 : {nList[5 : 11]}")

nList[10] = [0, 0, 0]
print(f"8 : {nList}")

for x in range(len(nList)):
    if type(nList[x]) is not int:
        nList[x] = x + 1
print(f"9 : {nList}")

nList_2 = nList.copy()
nList_2.sort(reverse = True)
print(f"10 : {nList_2}")

for y in range(len(nList)):
    if (nList[y]) % 2 == 0:
        nList[y] = nList[y] * 10
print(f"11 : {nList}")

numMat = [[0 for c in range(10)] for r in range(4)]
for q in range(4):
    for w in range(10):
        numMat[q][w] = nList[cnt_index]
        cnt_index += 1
print(f"12 : {numMat}")

numMat_1 = numMat[0][:]
print(f"13 : {numMat_1}")

for t in range(len(numMat_1)):
    sum += numMat_1[t]
numMat_1[-1] = sum
print(f"14 : {numMat_1}")

while len(numMat_1) != 1:
    sum_2 += numMat_1.pop(-1)
print(f"15 : 총합({sum_2}), 남은 리스트({numMat_1})")
# =============================================================================
import random as r
top = 0
low = 100
s_sum = 0
sList = list(range(100))
for i in range(100):
    sList[i]= r.randint(0, 100)
    s_sum += sList[i]
    if sList[i] > top:
        top = sList[i]
    if sList[i] < low:
        low = sList[i]
print(f"16 : {sList}")
print(f"최고 : {top} 최하 : {low} 평균 : {s_sum / 100}")
    