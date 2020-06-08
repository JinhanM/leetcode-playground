class Solution(object):
    def reverseString_n(self, s):

        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        def recr(l):
            if len(l) <= 1:
                return l
            else:
                return recr(l[1:]) + [l[0]]
        s[:] = recr(s)

    def reverseString_1(self, s):
        def helper(start, end, ls):
            if start >= end:
                return

            # swap the first and last element
            ls[start], ls[end] = ls[end], ls[start]

            return helper(start + 1, end - 1, ls)

        helper(0, len(s) - 1, s)


test = Solution()
test.reverseString_1(["h","e","l","l","o"])
