class Solution(object):
    def sumOfDigits(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        return sum(map(int, str(min(A)))) & 1 ^ 1