#User function Template for python3

class Solution:
    def sumOfMatrix(self,N,M,Grid):
        #code here
        return sum(sum(rows) for rows in Grid)
