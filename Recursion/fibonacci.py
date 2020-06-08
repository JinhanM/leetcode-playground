class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        cache = {}
        cache[0] = 0
        cache[1] = 1
        for i in range(2, N+1):
            cache[i] = cache[i-1] + cache[i-2]
        return cache[N]
