class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a_count = 0
        l_consecutvie_count = 0

        for c in s:
            if c == "A":
                if a_count == 1:
                    return False
                a_count += 1
                l_consecutvie_count = 0
            elif c == "L":
                if l_consecutvie_count == 2:
                    return False
                l_consecutvie_count += 1
            else:
                l_consecutvie_count = 0
        return True
            