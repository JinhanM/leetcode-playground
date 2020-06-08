# 两两交换链表中的节点
# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
#
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Check node
        if not head or not head.next:
            return head
        # Record
        p = head.next
        head.next = self.swapPairs(head.next.next)
        p.next = head
        return p

    def swapPairs_faster(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next, curr = head, dummy
        while curr.next and curr.next.next:
            first, second = curr.next, curr.next.next
            curr.next, first.next, second.next = second, second.next, first

            curr = curr.next.next
        return dummy.next
