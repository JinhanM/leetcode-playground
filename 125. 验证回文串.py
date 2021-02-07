class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        sgood = "".join(ch.lower() for ch in s if ch.isalnum())
        i, j = 0, len(sgood)-1
        while i < j:
            if sgood[i] != sgood[j]:
                return False
            i += 1
            j -= 1
        return True