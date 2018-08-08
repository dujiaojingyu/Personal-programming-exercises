__author__ = "Narwhale"

class Node(object):
    """节点"""
    def __init__(self,elem):
        self.elem = elem
        self.next = None

# node = Node(100)
# node1 = Node(100)

class Singlelinklist(object):
    """单链表"""
    def __init__(self,node=None):
        self._head = node

    def is_empty(self):
        """链表是否为空"""
        return self._head == None

    def length(self):
        """链表长度"""
        cur = self._head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历整个链表"""
        cur = self._head
        while cur != None:
            print(cur.elem,end=" ")
            cur = cur.next



    def add(self,item):
        """向链表头部添加元素"""
        node = Node(item)
        node.next = self._head
        self._head = node


    def append(self,item):
        """向链表尾部添加元素"""
        node = Node(item)
        if self.is_empty():
            # 存放第一个元素
            self._head = node
        else:
            #cur相当于指针最先指向链表第一个元素
            cur = self._head
            #如果下一个元素不为None则循环到下一个
            while cur.next != None:
                #循环到下一个
                cur = cur.next
            #到了链表最后一个将添加元素的地址链接到最后一个元素的next属性
            cur.next = node

    def insert(self,pos,item):
        """指定位置添加元素"""
        node = Node(item)
        if pos <= 0:
            self.add(item)
        elif pos > self.length()-1:
            self.append(item)
        else:
            cur = self._head
            count = 0
            while count < (pos-1):
                cur = cur.next
                count += 1
            node.next = cur.next
            cur.next = node

    def remove(self,item):
        """删除节点"""
        cur = self._head
        while cur.elem != item:
            if cur.next == None:
                #如果循环了整个链表不存在就报错
                raise ValueError("%s not in list"%item)
            cur = cur.next
        else:
            cur.elem = cur.next.elem
            cur.next = cur.next.next



    def search(self,item):
        """查询节点是否存在"""
        cur = self._head
        while  cur != None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False



if __name__ == "__main__":
    ll = Singlelinklist()
    # print(ll.is_empty())
    # print(ll.length())
    #
    # ll.append(1)
    # print(ll.is_empty())
    # print(ll.length())

    # ll.append(2)
    # ll.append(3)
    # ll.append(4)
    # ll.append(5)
    # ll.add(9)
    # ll.insert(4,8)
    # ll.insert(2,8)
    print(ll.search(6))
    # ll.remove(9)
    # ll.travel()