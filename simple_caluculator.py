# 간단한 calculation
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "0으로 나눌 수 없습니다."
    return x / y

print("연산을 선택하세요:")
print("1. 덧셈")
print("2. 뺄셈")
print("3. 곱셈")
print("4. 나눗셈")

choice = input("선택 (1/2/3/4): ")

num1 = float(input("첫 번째 숫자: "))
num2 = float(input("두 번째 숫자: "))

if choice == '1':
    print(f"결과: {add(num1, num2)}")
elif choice == '2':
    print(f"결과: {subtract(num1, num2)}")
elif choice == '3':
    print(f"결과: {multiply(num1, num2)}")
elif choice == '4':
    print(f"결과: {divide(num1, num2)}")
else:
    print("잘못된 선택입니다.")