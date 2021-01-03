# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        p = front = ListNode(0)
        q = back = ListNode(0)
        while head:
            if head.val < x:
                front.next = head
                front = front.next
            else:
                back.next = head
                back = back.next
            head = head.next
        
        back.next = None
        front.next = q.next
        return p.next


        