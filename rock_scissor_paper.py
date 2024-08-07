
import random

choices = ["가위", "바위", "보"]
computer_choice = random.choice(choices)
user_choice = input("가위, 바위, 보 중 하나를 선택하세요: ")

if user_choice == computer_choice:
    print(f"비겼습니다! 컴퓨터도 {computer_choice}를 선택했습니다.")
elif (user_choice == "가위" and computer_choice == "보") or \
     (user_choice == "바위" and computer_choice == "가위") or \
     (user_choice == "보" and computer_choice == "바위"):
    print(f"이겼습니다! 컴퓨터는 {computer_choice}를 선택했습니다.")
else:
    print(f"졌습니다. 컴퓨터는 {computer_choice}를 선택했습니다.")
