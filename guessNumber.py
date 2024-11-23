import random


def play_game()->None:
    print("===========猜數字遊戲===========")
    min=1
    max=100
    target=random.randint(1,100)
    print(target)
    guessCount=0
    while True:
        try:
            myguess=int(input(f"請在{min}~{max}內猜一個正整數:"))
            if myguess<0 or myguess>100:
                continue
        except Exception:
            print("請輸入正整數")
            continue
        else:
            if myguess<target:
                guessCount+=1
                min=myguess
                print(f"你已經猜了{guessCount}次，請猜大一點")
            elif myguess>target:
                guessCount+=1
                max=myguess
                print(f"你已經猜了{guessCount}次，請猜小一點")
            else:
                print("猜中了")
                break

while True:
    play_game()
    
    myinput=input("要繼續玩嗎?(y/n)")
    while myinput!='y' and myinput!='n':
        myinput=input("要繼續玩嗎?(y/n)")
    if myinput=='n':
        break
print("遊戲結束")