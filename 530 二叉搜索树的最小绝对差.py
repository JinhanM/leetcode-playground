# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        self.curr_min = float("inf")
        self.pre = None

        # staticmethod
        def helper(node):
            if not node:
                return
            helper(node.left)
            if self.pre is not None:
                self.curr_min = min(self.curr_min, node.val - self.pre)
            self.pre = node.val
            helper(node.right)
        helper(root)
        return self.curr_min