#User function Template for python3
class Solution:
    def consecutiveSum (self, n):
        # code here 
        if (n-3)%3==0:
            n=(n-3)//3
            return [n,n+1,n+2]
        else:
            return [-1]
