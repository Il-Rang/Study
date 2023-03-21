'''
print("\n줄바꿈\n연습")
print("\t탭키\t연습")
print("어떤 글자를 \"강조\"하는 효과1")
print("어떤 글자를 \'강조\'하는 효과1")
print("\\\\ 백슬래시 2개 출력")
    
#=================

product1, product2 = map(int, input("서로 곱할 수 두개를 입력하시오 : ").split())
result = product1 * product2
print(f'{product1} x {product2} = {result}')
    
#=================

string1 = input("첫 번째 문자열을 입력 → ")
st_len1 = len(string1)
string2 = input("두 번째 문자열을 입력 → ")
st_len2 = len(string2)
diff = st_len1 - st_len2
print(f"두 문자열의 길이 차이는 {abs(diff)}입니다.")
    
#=================

# upper lower isupper islower conut find("찾을 단어", 시작 위치)
string1 = input("첫 번째 문자열을 입력 → ") # maple을 입력
string2 = input("두 번째 문자열을 입력 → ") # MAPLE을 입력
print(f"{string1.upper()}")
print(f"{string2.lower()}")
print(f"{string1.isupper()}")
print(f"{string2.islower()}")
st_count = string1.count("m")
print(f"{st_count}")
st_find = string1.find("m")
print(f"{st_find}")
'''
string = input("문자열을 입력 → ")
count = len(string)
for i in range(count):
    print(f"{string[i]}")