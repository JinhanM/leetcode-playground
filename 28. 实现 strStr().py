class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) == 0:
            return 0
        if len(haystack) < len(needle):
            return -1

        i, j = 0, 0
        while i < len(haystack):
            if haystack[i] == needle[j]:
                if j == len(needle) - 1:
                    return i-j
                i += 1
                j += 1
            else:
                if j != 0:
                    i = i-j+1
                    j = 0
                else:
                    i += 1

        return -1