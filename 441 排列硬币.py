from math import sqrt
class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = ((1+8*n)**0.5-1)/2
        return int(res)