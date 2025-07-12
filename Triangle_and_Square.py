#User function Template for python3

class Solution:
    def countShare(self,B):
        #code here
        A=B//2
        count_of_squares = A*(A-1)//2
        return count_of_squares
