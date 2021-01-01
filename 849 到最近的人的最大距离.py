class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        ans = 1
        prev = -1
        for i, seat in enumerate(seats):
            if seat:
                if prev >= 0:
                    ans = max(ans, (i-prev)/2)
                else:
                    ans = i
                prev = i
        return max(ans, len(seats)-1-prev)