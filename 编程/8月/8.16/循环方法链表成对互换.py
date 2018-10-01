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
        #建立辅助空的头结点很重要
        h = ListNode(0)
        h.next = self.__head
        head = h
        #         node1        node2
        # head------1-------------2-------3--------4-------Null
        #建立两个节点分别在要交换的第一个和第二个
        while head.next and head.next.next:
            node1 = head.next
            print(node1.elem)  #1
            node2 = node1.next

            head.next = node2
            node1.next = node2.next
            node2.next = node1
            head = node1


        return h.next



    #         node1        node2
    #head------1-------------2-------3--------4-------Null


if __name__ == "__main__":
    ll = Solution()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    ll.travel()
    print('----\n')
    print(ll.swapPairs())

    ll.travel()


