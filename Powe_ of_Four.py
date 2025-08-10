# you may use python module's
# just return true/false or 1/0
class Solution():
    def isPowerofFour(self, n):
         # code here
            if n<=0:
                return 0
            while(n%4==0):
                n=n//4
            return n==1
