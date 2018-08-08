__author__ = "Narwhale"

class Node(object):
    """节点"""
    def __init__(self,elem):
        self.elem = elem
        self.next = None


class Singlelinklist(object):
    """链表"""
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
            cur = cur.next
            count += 1
        return count

    def travel(self):
        """遍历整个链表"""
        cur = self._head
        while cur != None:
            print(cur.elem,end=" ")
            cur = cur.next



    def add(self,item):
        """向链表头部添加元素"""
        cur = self._head
        node = Node(item)
        node.next = cur
        self._head = node



    def append(self,item):
        """向链表尾部添加元素"""
        node = Node(item)
        if self.is_empty():
            self._head = node
        else:
            cur = self._head
            while cur.next != None:
                cur = cur.next
            cur.next = node


    def insert(self,pos,item):
        """指定位置添加元素"""
        cur = self._head
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
        cur = self._head
        count = 0
        while cur.elem != item:
            if cur.next == None:
                raise ValueError("%s not in list"%item)
            cur = cur.next
        cur.elem = cur.next.elem
        cur.next = cur.next.next

    def search(self,item):
        """查询节点是否存在"""
        cur = self._head
        while cur != None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
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
    ll.insert(5,8)
    ll.remove(9)
    print(ll.search(-1))
    ll.travel()

