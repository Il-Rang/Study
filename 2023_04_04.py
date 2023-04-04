# numtup1 = (10, 20, 30)
# print(numtup1)
# numtup2 = (10)
# print(numtup2)
# numtup3 = (10, )
# print(numtup3)
# del(numtup1, numtup2, numtup3)

# numtup = (10, 20, 30, 40, 50)
# print(numtup[0])
# print(numtup[:])
# print(numtup[3:])
# print(numtup[:3])

# mytup = (10, 20, 30)
# mylist = list(mytup)
# mylist.append(40)
# mytup = tuple(mylist)
# print(mytup)

# idol = {}
# idol['이름'] = input("이름을 입력하시오 : ")
# idol['구성원 수'] = int(input("구성원의 수를 입력하시오 : "))
# idol['데뷔'] = input("데뷔 프로그램을 입력하시오 : ")
# idol['대표곡'] = input("대표곡을 입력하시오 : ")

# for k in idol.keys() :
#     print(k, " ==> ", idol[k])

items = {}
print("물품과 재고량 입력")
while True:
    item = input("입력 물품 : ")
    if item == '':
        break
    else:
        items[f'{item}'] = int(input("재고량 : "))

print("물품과 재고량 확인")
while True:
    fitem = input("찾을 물품 : ")
    if fitem == '':
        break
    elif fitem in items:
        print(f'{items[fitem]}개 남았어요.')
    else:
        print('그 물품은 없어요.')