class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr = 0

        for i in range(1, len(nums)):
            if nums[i] != nums[curr]:
                nums[curr+1] = nums[i]
                curr += 1
        return curr+1