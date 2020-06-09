# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)

        def merge_helper(l1, l2, curr):
            if not l1 or not l2:
                if not l1:
                    curr.next = l2
                if not l2:
                    curr.next = l1
            else:
                if l1.val < l2.val:
                    curr.next = l1
                    merge_helper(l1.next, l2, curr.next)
                else:
                    curr.next = l2
                    merge_helper(l2.next, l1, curr.next)

        merge_helper(l1, l2, dummy)
        return dummy.next
