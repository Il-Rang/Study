import turtle as t

# 실습_1
n1 = int(input("첫 번째 숫자를 입력 → "))
n2 = int(input("두 번째 숫자를 입력 → "))
print(f"{n1} + {n2} = {n1 + n2}")
print(f"{n1} - {n2} = {n1 - n2}")
print(f"{n1} × {n2} = {n1 * n2}")
print(f"{n1} ÷ {n2} = {n1 / n2}")
print(f"{n1} % {n2} = {n1 % n2 : .5f}")
print(f"{n1} ^ {n2} = {n1 ** n2}")

# 실습_2
t.shape("turtle")
t.pensize(5)
t.pencolor("pink")

n = int(input("그리실 도형의 각의 개수를 입력하시오 : "))
for i in range(n):
    t.right(360 / n)
    t.forward(1000 / n)
t.done()

# 실습_3
for i in range(1, 51):
    astr = "*" * i
    print(f"{astr}")