# import os

# numlist = []
# sum = 0

# while True:
#     os.system('cls')
#     print(f'현재 리스트에 저장된 값 : {numlist}')
#     print("리스트를 수정하려면 아래 중 하나를 선택하세요:\n1. 값 추가하기\n2. 값 삭제하기\n3. 수정 종료하기")
#     sel = int(input("선택한 번호를 입력하세요 : "))
#     os.system('cls')

#     if sel == 1:
#         count_1 = int(input("리스트에 몇 개의 값을 추가하시겠습니까? : "))
#         for i in range (count_1):
#             print(f'현재 리스트에 저장된 값 : {numlist}')
#             numlist.append(int(input("리스트에 추가할 값을 입력하세요 : ")))
#             os.system('cls')

#     elif sel == 2:
#         count_2 = int(input("리스트에서 몇 개의 값을 삭제하시겠습니까? : "))
#         for j in range (count_2):
#             print(f'현재 리스트에 저장된 값 : {numlist}')
#             del numlist[int(input("삭제할 값의 인덱스를 입력하세요 : "))]
#             os.system('cls')

#     elif sel == 3:
#         break

#     else:
#         print("제대로 된 값을 입력하세요.")

# print(f"리스트에 저장된 값 : {numlist}")

# for x in range(len(numlist)):
#     sum += numlist[x]

# print(f"리스트에 저장된 값의 합 : {sum}")

# f = open("03.28.list.txt", 'w', encoding = "UTF-8")
# f.write(f"리스트에 저장된 값 : {numlist}, 리스트에 저장된 값의 합 : {sum}")
# f.close()

# # =============================================================================

# numList = [[1, 2, 3, 4],
#            [5, 6, 7, 8],
#            [9, 10, 11, 12]
#            ]
# for i in range(0, 3):
#     for j in range(0, 4):
#         print(numList[i][j], end = ' ')
#     print("")

# # =============================================================================

nList = list(range(10)) # 0 ~ 9까지의 값을 지닌 리스트를 생성
print(f"1 : {nList}")

nList[1] = 100 # 1번 인덱스의 값을 100으로 변경
print(f"2 : {nList}")

sum =  0 # 리스트 내 값의 합을 출력
for i in nList:
    sum += i
print(f"3 : {nList}")

nList[2] = "not number" # 2번 인덱스의 값을 "not number"로 변경
print(f"4 : {nList}")

for j in range(10, 21): # 리스트에 10 ~ 20까지의 값을 추가
    nList.append(j)
print(f"5 : {nList}")

print(f"6 : {len(nList)}") # 리스트의 크기를 출력

print(f"7 : {nList[10:-1]}") # 10번 인덱스부터 마지막까지의 값을 출력
print(f"8 : {nList[0:2]}") # 0번 인덱스 부터 2번 인덱스까지의 값을 출력

for x in range(len(nList)): # 값이 문자열인 인덱스를 찾아 값을 인덱스로 변경
    if type(nList[x]) is str:
        print(f"9 : {x}번 인덱스의 값이 문자열입니다.")
        nList[x] = x
print(f"9 : {nList}")

nList = [i for i in nList if i < 10] # 리스트 내 10이상의 값을 삭제
print(f"10 : {nList}")

# # =============================================================================