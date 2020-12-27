class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        r_matrix = [[0 for i in range(len(A))] for _ in range(len(A[0]))]

        for i in range(len(A)):
            for j in range(len(A[0])):
                r_matrix[j][i] = A[i][j]
        return r_matrix