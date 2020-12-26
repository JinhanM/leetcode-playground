class Solution:
    def numWays(self, n, relation, k):
    	"""
        :type n: int
        :type relation: List[List[int]]
        :type k: int
        :rtype: int
        """
        dp = [0] * n
        dp[0] = 1

        for i in range(k):
            curr = [0]*n
            for last, nxt in relation:
                curr[nxt] += dp[last]
            dp = curr
        return curr[n-1]