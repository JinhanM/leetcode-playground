class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        temp = [num ** 2 for num in nums]
        return sorted(temp)