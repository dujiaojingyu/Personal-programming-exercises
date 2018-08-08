
age = 56
count = 0
while count < 3:
    guess_age = int(input("age:"))
    if guess_age == age:
        print("lucky you,you get it..")
        break
    elif guess_age < age:
        print("think smaller....")
    else:
        print("think bigger....")

    count +=1

else:                                        #当while部分不成立时运行else部分，如：当guess次数超过三次就会运行
    print("you have tried too many times ...")
