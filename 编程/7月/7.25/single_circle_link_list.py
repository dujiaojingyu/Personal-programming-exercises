__author__ = "Narwhale"

class Node(object):
    """节点"""
    def __init__(self,elem):
        self.elem = elem
        self.next = None


class Singlelinklist(object):
    """链表"""
    def __init__(self,node=None):
        self.__head = node
        if node:
            node.next = node


    def is_empty(self):
        """链表是否为空"""
        return self.__head == None

    def length(self):
        """链表长度"""
        if self.is_empty():
            return 0
        cur = self.__head
        count = 1
        while cur.next != self.__head:
            cur = cur.next
            count += 1
        return count

    def travel(self):
        """遍历整个链表"""
        if self.is_empty():
            return
        else:

            cur = self.__head
            while cur.next != self.__head:
                print(cur.elem,end=" ")
                cur = cur.next
            #退出循环为节点的elem未打印
            print(cur.elem)
            print("")



    def add(self,item):
        """向链表头部添加元素"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next

            node.next = self.__head
            self.__head = node
            cur.next = self.__head


###########################
    def append(self,item):
        """向链表尾部添加元素"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            node.next = self.__head
            cur.next = node


    def insert(self,pos,item):
        """指定位置添加元素"""
        cur = self.__head
        node = Node(item)
        count = 0
        if pos <= 0:
            self.add(item)
        elif pos > self.length()-1:
            self.append(item)
        else:
            while count < pos-1:
                count += 1
                cur = cur.next
            node.next = cur.next
            cur.next = node



    def remove(self,item):
        """删除节点"""
        # cur = self.__head
        # count = 0
        # while cur.elem != item:
        #     # if cur == self.__head:
        #     #     self.__head = cur.next
        #     if cur.next == self.__head:
        #         raise ValueError("%s not in list"%item)
        #     cur = cur.next
        # if cur == self.__head:
        #     self.__head = cur.next
        #     while cur.next != self.__head:
        #         cur = cur.next
        #     cur.next = self.__head
        # elif cur.elem == item:
        #     cur.elem = cur.next.elem
        #     cur.next = cur.next.next

        if self.is_empty():
            return
        cur = self.__head
        per = None
        while cur.next != self.__head:
            if cur.elem == item:
                if cur == self.__head:
                    rear = self.__head
                    while rear.next != self.__head:
                        rear = rear.next
                    self.__head = cur.next
                    rear.next = self.__head
                else:
                    per.next = cur.next
                return
            else:
                per = cur
                cur = cur.next
        if cur.elem == item:
            if cur == self.__head:
                #链表只有一个节点
                self.__head = None
            else:
                per.next = cur.next


    def search(self,item):
        """查询节点是否存在"""
        if self.is_empty():
            return False
        cur = self.__head
        while cur.next != self.__head:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        #当 cur == self.__head推出循环不能判断最后一个是否存在，所以要加if判断
        if cur.elem == item:
            return  True
        return False



if __name__ == "__main__":
    ll = Singlelinklist()
    print(ll.is_empty())
    ll.append(1)

    print(ll.is_empty())


    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.add(9)
    ll.add(2)
    ll.add(4)
    ll.add(8)
    ll.insert(5,8)
    ll.remove(8)
    print(ll.search(-1))
    ll.travel()
