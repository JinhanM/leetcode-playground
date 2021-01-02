class Solution(object):
    def waysToStep(self, n):
        """
        :type n: int
        :rtype: int
        """
        base_case = [1,2,4]
        if n == 0:
            return 0
        if n <= 3:
            return base_case[n-1]
        prev_1, prev_2, prev_3, curr = base_case[0], base_case[1], base_case[2], 0
        for i in range(3, n):
            prev_1, prev_2, prev_3 = prev_2 % 1000000007, prev_3 % 1000000007, (prev_1+prev_2+prev_3)%1000000007

        return prev_3