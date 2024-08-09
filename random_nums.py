
# 숫자 맞추기 게임
import random

def get_random_num_game():
    number_to_guess = random.randint(1, 100)
    guess = None

    while guess != number_to_guess:
        guess = int(input("숫자를 맞춰보세요 (1-100): "))
        if guess < number_to_guess:
            print("더 큰 숫자입니다.")
        elif guess > number_to_guess:
            print("더 작은 숫자입니다.")
        else:
            print("정답입니다!")


import random
def generate_lotto_numbers():

    numbers = random.sample(range(1,46),6)
    numbers.sort()
    return numbers

if __name__ == "__main__":
    #get_random_num()
    lotto_numbers = generate_lotto_numbers()
    print("로또 번호:", lotto_numbers)
