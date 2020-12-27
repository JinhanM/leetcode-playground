class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if arr <= 2:
            return True
        arr = sorted(arr)
        diff = arr[1] - arr[0]
        i = 0
        while i < len(arr)-1:
            if arr[i+1] - arr[i] != diff:
                return False
            i += 1
        return True