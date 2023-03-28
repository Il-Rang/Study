import os

numlist = []
sum = 0

while True:
    os.system('cls')
    print(f'현재 리스트에 저장된 값 : {numlist}')
    print("리스트를 수정하려면 아래 중 하나를 선택하세요:\n1. 값 추가하기\n2. 값 삭제하기\n3. 수정 종료하기")
    sel = int(input("선택한 번호를 입력하세요 : "))
    os.system('cls')

    if sel == 1:
        count_1 = int(input("리스트에 몇 개의 값을 추가하시겠습니까? : "))
        for i in range (count_1):
            print(f'현재 리스트에 저장된 값 : {numlist}')
            numlist.append(int(input("리스트에 추가할 값을 입력하세요 : ")))
            os.system('cls')

    elif sel == 2:
        count_2 = int(input("리스트에서 몇 개의 값을 삭제하시겠습니까? : "))
        for j in range (count_2):
            print(f'현재 리스트에 저장된 값 : {numlist}')
            del numlist[int(input("삭제할 값의 인덱스를 입력하세요 : "))]
            os.system('cls')

    elif sel == 3:
        break

    else:
        print("제대로 된 값을 입력하세요.")

print(f"리스트에 저장된 값 : {numlist}")

for x in range(len(numlist)):
    sum += numlist[x]

print(f"리스트에 저장된 값의 합 : {sum}")
