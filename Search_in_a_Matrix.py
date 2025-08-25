#User function Template for python3

class Solution:
    
    #Function to search a given integer in a matrix.
    def searchMatrix(self,matrix, x): 
        # code here 
        for i in matrix:
            if x in i:
                return True
        return False
