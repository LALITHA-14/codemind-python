#User function Template for python3

class Solution:
    def sumOfSeries(self,n):
        #code here
        a=0
        for i in range(1,n+1):
            a+=i**3
        return a
