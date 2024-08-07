import random
import string

def generate_pass(length):
    char = string.ascii_letters  + string.digits + string.punctuation
    password = "".join(random.choice(char) for i in range(length))
    return password

while True:

    try:
        length = int(input('암호의 길이를 입력하세요: '))
        if length <= 0:
            print("길이는 0보단 커야 합니다. 다시 입력해주쇼")
        else:
            break
    except ValueError:
        print("유효한 숫자를 입력하쇼")

print(f"생성된 암호: {generate_pass(length)}")