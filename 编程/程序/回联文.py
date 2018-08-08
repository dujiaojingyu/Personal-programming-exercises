
def palindrome(str1):
    length = len(str1)
    last = length - 1
    length //= 2
    flag = 1
    for each in range(length):
        if str1[each] != str1[last]:
            flag = 0
        else:
            last -= 1

    if flag == 1:
        print('是回联文')
    else:
        print('不是回联文')
    
str1 = input("请输入一个句子：")
palindrome(str1)
