import random
import time

options = ['가위', '바위', '보']

ascii_art = {
    '가위': """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""",
    '바위': """
    _______
---'   ____)
      (_____)
      (_____)
      (_____)
---.__(___)
""",
    '보': """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""
}

ascii_art_reversed = {
    '가위': """
        _______
  ____(____   '--- 
 (______
 (__________
      (____)
       (___)__.---
""",
    '바위': """
        _______
       (____   '--- 
     (_____)
     (_____)
     (_____)
       (___)__.---
""",
    '보': """
        _______
  ____(____   '--- 
 (______
  (_______
   (_______
       (__________.---
"""
}

def main():
    computer_choice = random.choice(options)

    # 사용자에게 선택을 요청합니다
    user_choice = input('가위, 바위, 보 중 하나를 선택하세요: ')

    # 사용자의 선택이 유효한지 확인합니다
    while user_choice not in options:
        print('잘못된 선택입니다')
        user_choice = input('가위, 바위, 보 중 하나를 다시 선택하세요: ')

    # 사용자의 선택을 출력합니다
    print("당신의 선택:")
    print(ascii_art[user_choice])

    # 로딩 패널을 출력합니다
    print('컴퓨터가 선택 중입니다', end='', flush=True)
    for _ in range(5):
        time.sleep(0.5)
        print('.', end='', flush=True)
    print('\r컴퓨터가 선택 중입니다... 완료!', flush=True)

    # 컴퓨터의 선택을 오른쪽에서 나오는 애니메이션으로 출력합니다
    print("컴퓨터의 선택:")
    for line in ascii_art_reversed[computer_choice].split('\n'):
        print(f"{' ' * 20}{line}")
        time.sleep(0.1)

    # 승자를 결정합니다
    if computer_choice == user_choice:
        print('비겼습니다!')
    elif computer_choice == '바위' and user_choice == '가위':
        print('컴퓨터가 이겼습니다!')
    elif computer_choice == '보' and user_choice == '바위':
        print('컴퓨터가 이겼습니다!')
    elif computer_choice == '가위' and user_choice == '보':
        print('컴퓨터가 이겼습니다!')
    else:
        print('당신이 이겼습니다!')

# 메인 함수를 호출합니다
main()