# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        def dfs_helper(root):
            if not root:
                return -1
            depth = max(dfs_helper(root.left), dfs_helper(root.right))+1
            if depth == len(res):
                res.append([])
            res[depth].append(root.val)
            return depth
        
        dfs_helper(root)
        return res