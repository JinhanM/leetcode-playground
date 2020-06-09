import math


class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        def quick_mul(N):
            if N == 0:
                return 1.0
            y = quick_mul(N // 2)
            if N % 2 == 0:
                return y * y
            return y * y * x

        if n >= 0:
            return quick_mul(n)
        return 1 / quick_mul(-n)

    def notMyPow(self, x, n):
        return math.pow(x, n)
