# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.count = 0

        # staticmethod
        def helper(node, currmax):
            if not node:
                return 
            else:
                if node.val >= currmax:
                    self.count += 1
                    currmax = node.val
                helper(node.left, currmax)
                helper(node.right, currmax)
        
        helper(root, -float("inf"))
        return self.count

                