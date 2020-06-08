class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        cache = {}
        cache[1], cache[2] = 1, 2
        for i in range(3, n+1):
            cache[i] = cache[i-1] + cache[i-2]
        return cache[n]

    def climbStairs_faster(self, n):
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2

        n1, n2 = 1, 2
        res = 0
        for i in range(n+1):
            res = n1 + n2
            n1, n2 = n2, res
        return res
