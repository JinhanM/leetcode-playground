class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        return eval("*".join(str(n))) - eval("+".join(str(n)))