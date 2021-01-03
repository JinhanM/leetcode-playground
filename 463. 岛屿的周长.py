class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    if i-1<0 or grid[i-1][j]==0:
                        ans+=2
                    if j-1<0 or grid[i][j-1]==0:
                        ans+=2
        return ans