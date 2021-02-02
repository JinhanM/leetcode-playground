class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for i, num in enumerate(nums):
            if num in hashmap:
                return [i, hashmap[num]]
            else:
                hashmap[target-num] = i
        return -1