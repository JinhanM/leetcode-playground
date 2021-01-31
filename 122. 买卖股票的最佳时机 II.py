class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        profit = 0
        curr_max = prices[0]
        for i in range(1, len(prices)):
            curr = prices[i]
            if curr_max < curr:
                profit += curr - curr_max
                curr_max = curr
            else:
                curr_max = curr
        return profit