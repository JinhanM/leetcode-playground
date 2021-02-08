class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        s, l = min(strs), max(strs)
        for i in range(len(s)):
            if s[i] != l[i]:
                return s[:i]
        return s