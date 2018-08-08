age = 56
for i in range(3):
    guess_age = int(input("age:"))
    if guess_age == age:
        print("lucky you,you get it..")
        break
    elif guess_age < age:
        print("think smaller....")
    else:
        print("think bigger....")

else:                                        #当正常运行完成时else部分才运行，当被break时就不能运行了
    print("you have tried too many times ...")
