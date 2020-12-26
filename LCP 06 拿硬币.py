class Solution(object):
    def minCount(self, coins):
        """
        :type coins: List[int]
        :rtype: int
        """
        total = 0
        for coin in coins:
            total += coin // 2
            total += coin % 2
        return total