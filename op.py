i=0

while True:
    try:
        i+=int(input("請輸入數值"))
        again=input("繼續玩?(y/n)")
        
        if again=='n':
            break            
    except Exception:
        print("請輸入整數")
        continue
    print(i)