class Solution:

    def colSum(self, mat):
        # Code here
        if not mat or not mat[0]:
            return []
        n=len(mat)
        m=len(mat[0])
        result=[0]*m
        for i in range(n):
            for j in range(m):
                result[j]+=mat[i][j]
        return result
