
def findstr(constr,substr):
    
    count = 0
    length = len(constr)

    if substr not in constr:
        print("未在目标字符串中找到字符串")
    else:
        for each in range(length-1):
            if constr[each] == substr[0]:
                if constr[each+1] == substr[1]:
                    count += 1
           
                
        print("子字符串在目标字符串中出现%d次"%count)        
    
        
constr = input("请输入要检测的字符串内容：")
substr = input("请输入要检测的字符串（两个字符串）：")

findstr(constr,substr)
