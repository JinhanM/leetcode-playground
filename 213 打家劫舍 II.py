class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        def rob_helper(nums):
            pre, currmax = 0, 0
            for num in nums:
                currmax, pre = max(currmax, pre+num), currmax
            return currmax
    
        return max(rob_helper(nums[1:]), rob_helper(nums[:-1]))