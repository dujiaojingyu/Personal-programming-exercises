class MyArray:
    '''All the elements in this array must be numbers'''
    #判断是否是数字
    def __IsNumber(self,n):
        if not isinstance(n,(int,float,complex)):
            return False
        return True

    def __init__(self , *args):
        #构造函数进行必要的初始化
        if not args:
            self.__value = []
        else:
            for arg in args:
                if not self.__IsNumber(arg):
                    print("All elements must be numbers")
                    return
            self.__value = list(args)

    def __del__(self):
        #析构函数，释放内部封装的列表
        del self.__value

    #重写运算符+
    def __add__(self, n):
        if self.__IsNumber(n):
            #数组中所有元素加n
            b = MyArray()
            b.__value = [item+n for item in self.__value]
            return b
        elif isinstance(n,MyArray):
            if len(n.__value) == len(self.__value):
                c = MyArray()
                c.__value = [i+j for i,j in zip(self.__value,n.__value)]
                return c
            else:
                print("Length not equal")
        else:
            print("Not supported")

    def __len__(self):
        return len(self.__value)

    def __repr__(self):
        return repr(self.__value)

    def __str__(self):
        return str(self.__value)


if __name__ == "__main__":
    print("Please use me as a module")


