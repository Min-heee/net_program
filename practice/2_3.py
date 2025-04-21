from random import randint

def auto_coin_flip_game():
    money = 50  # 초기 자금 $50
    print(f"게임 시작! 현재 자금: ${money}")
    
    while 0 < money < 100:
        # 플레이어 예측 자동 생성 (1 또는 2)
        guess = randint(1, 2)
        print(f"\n플레이어 예측: {'앞면' if guess == 1 else '뒷면'}({guess})")
        
        # 동전 던지기 결과
        coin = randint(1, 2)
        print(f"동전 결과: {'앞면' if coin == 1 else '뒷면'}({coin})")
        
        # 결과 판정
        if guess == coin:
            money += 9
            print(f"맞췄습니다! +$9 (현재 자금: ${money})")
        else:
            money -= 10
            print(f"틀렸습니다! -$10 (현재 자금: ${money})")
    
    # 게임 종료 조건 확인
    if money <= 0:
        print("\n게임 오버! 모든 돈을 잃었습니다.")
    else:
        print("\n축하합니다! $100을 달성하여 게임에서 승리하셨습니다!")

# 게임 실행
if __name__ == "__main__":
    auto_coin_flip_game()