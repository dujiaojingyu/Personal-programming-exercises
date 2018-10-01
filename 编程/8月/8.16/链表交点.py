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
    def length(self):
        """求长度"""
        cur = self.__head
        count = 0
        while cur is not None:
            cur = cur.next
            count += 1
        return count

# def cross_node(link1,link2):
#     """求交叉的节点"""
#     length1 = link1.length()
#     length2 = link2.length()
#     print(link1)
#     print(link2)






if __name__ == "__main__":
    l1 = Solution()
    l1.append(1)
    l1.append(3)
    l1.append(5)
    l1.append(7)
    l1.append(9)
    l1.append(12)
    l1.append(13)
    l1.travel()
    print('\n')
    l2 = Solution()
    l2.append(2)
    l2.append(4)
    l2.append(6)
    l2.append(8)
    l2.append(10)
    l2.append(11)
    l2.append(12)
    l2.append(13)
    l2.travel()
    print('\n')
    c= cross_node(l1,l2)




