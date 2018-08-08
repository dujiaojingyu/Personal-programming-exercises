# _*_ coding: utf-8 _*_
# 程序 7-13 (Python 3 version )
import os
class_101 = dict() #记录学生座号及姓名
chi_score = dict() #记录语文成绩
eng_score = dict() #记录英语成绩
mat_score = dict() #记录数学成绩
subjects = ["语文", "英语", "数学"]
scores  = [chi_score, eng_score, mat_score]

def disp_menu():
    os.system("clear")
    print("Class 101班级成绩管理系统")
    print("-------------------------")
    print("1. 输入学生姓名")
    print("2. 输入语文成绩")
    print("3. 输入英语成绩")
    print("4. 输入数学成绩")
    print("5月. 显示成绩单")
    print("0. 结束程序")
    print("-------------------------")

def enter_std_data():
    while True:
        no = int(input("座号（0==>停止输入）："))
        if no <=0 or no >100: break
        name = input("姓名：")
        class_101[no] = name
        print(class_101)

def enter_score(subject_no):
    for no, name in class_101.items():
        scores[subject_no][no] = \
          int(input("{},{}的{}成绩:". \
            format(no, name, subjects[subject_no])))
    print(scores[subject_no])
    x = input("按Enter返回主菜单")

def disp_score_table():
    for no in class_101.keys():
        print("{:<5}:".format(class_101[no]), end="")
        sum = 0
        for subject_no in range(0,3):
            sum = sum + scores[subject_no][no]
            print("{}:{:>3} ".format(subjects[subject_no], \
              scores[subject_no][no]), end="")
        print("总分:{:>3}, 平均:{:.2f}".format(sum, \
          float(sum)/len(scores)))
    x = input("按Enter返回主菜单")


### 主程序从这里开始

while True:
    disp_menu()
    user_choice = int(input("请输入您的选择："))
    if user_choice==1:
        enter_std_data()
    elif user_choice>=2 and user_choice<=4:
        enter_score(user_choice-2)
    elif user_choice==5:
        disp_score_table()
    else:
        break
print("谢谢您的使用，再见！")
