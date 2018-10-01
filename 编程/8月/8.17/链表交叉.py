__author__ = "Narwhale"

# 遍历两个链表到最后，判断连个链表最后的位置是否相同，不同直接返回；用两个变量记录链表的长度，哪个长
#  先往后遍历到一样长，接着另一个也开始同时遍历，直到相等，返回头指针

class Solution(object):

    def length(self, head):
        cur = head
        count = 0
        while cur:
            cur = cur.next
            count += 1
        return count

    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        if headA == None or headB == None:
            return None

        length1 = self.length(headA)
        length2 = self.length(headB)

        if length1 >= length2:
            for i in range(length1 - length2):
                headA = headA.next

        else:
            for i in range(length2 - length1):
                headB = headB.next

        min_len = min(length1, length2)

        for i in range(min_len):
            if headA == headB:
                return headA
            else:
                headA = headA.next
                headB = headB.next
        return None
