class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        length =len(nums)
        nums[:]= nums[-(k%length):]+nums[0:-(k%length)]