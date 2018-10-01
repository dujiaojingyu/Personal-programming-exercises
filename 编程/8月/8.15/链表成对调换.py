__author__ = "Narwhale"

class ListNode:
    def __init__(self,elem):
        self.elem = elem
        self.next = None

class Solution(object):
    def __init__(self,node=None):
        self.__head = node

    def is_empty(self):
        return self.__head == None

    def append(self,item):
        node = ListNode(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next is not None:
                cur = cur.next
            cur.next = node

    def travel(self):
        """遍历整个链表"""
        cur = self.__head
        while cur != None:
            print(cur.elem,end=" ")
            cur = cur.next

    def swapPairs(self):
        if self.__head == None or self.__head.next == None:
            return self.__head
        node = self.__head
        result = node.next
        while node and node.next:
            temp = node.next
            node.next = temp.next
            temp.next.next = temp.next
            temp.next = None
            self.__head = temp
            return self.__head




if __name__ == "__main__":
    ll = Solution()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.travel()
    print('\n')
    print(ll.swapPairs())

    ll.travel()
