# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0, head)
        front, back = dummy, head
        for _ in range(n):
            back = back.next
        
        while back:
            back = back.next
            front = front.next
        
        front.next = front.next.next
        return dummy.next