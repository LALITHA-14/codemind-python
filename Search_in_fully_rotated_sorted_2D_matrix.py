class Solution:
    def searchMatrix(self, mat, x):
        # code here
        for row in mat:
            for val in row:
                if val==x:
                    return True
        return False
