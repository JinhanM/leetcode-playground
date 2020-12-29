class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        if len(arr) == 1:
            return arr[0]

        l = len(arr)
        window = len(arr)//4
        for i in range(len(arr)-window):
            if arr[i] == arr[i+window]:
                return arr[i]
