def get_status(bmi->float)->str:
    pass


while True:
    try:
        height = float(input('請輸入身高(cm):'))
        weight= float(input('請輸入體重(kg):'))
        if  height<0 or weight<0:
            raise Exception
    except ValueError:
        print("使用者輸入錯誤，請重新輸入")
    except Exception:
        print("使用者輸入負數，身高體重不能為負數，請從新輸入")
        continue
    else:    
        BMI=weight/((height/100)**2)
        print(f"BMI值:{BMI}")
        if BMI >=35:
            print("重度肥胖")
        elif BMI >=30:
            print("中度肥胖")
        elif BMI >=27:
            print("輕度肥胖")
        elif BMI >=24:
            print("過重肥胖")              
        elif BMI >=18.5:
            print("健康體重")
        while (EndProgram := input("重新輸入請按1，離開程式請按0: ")) not in ('1', '0'):
            print("無效輸入，請輸入1或0。")
        if EndProgram =='1':
            continue
        else:
            break
print("結束BMI運算程式")