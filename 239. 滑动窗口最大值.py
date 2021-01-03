from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        res = []
        que = deque()
        for i in range(len(nums)):
            while que and nums[que[-1]] <= nums[i]:
                que.pop()
            que.append(i)
            print(que)
            if que and que[0] < i - k + 1:
                que.popleft()
            if i + 1 >= k:
                res.append(nums[que[0]])
        return res
