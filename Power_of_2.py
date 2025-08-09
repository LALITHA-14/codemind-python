class Solution:
    def isPowerofTwo(self, n):
        # code here
        if n<=0:
            return False
        while(n%2==0):
            n=n//2
        return n==1
