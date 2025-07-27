#User function Template for python3
import math
class Solution:
    def isPerfect(self,N):
        #code here
        c=0
        original=N
        while(N>0):
            digit=N%10
            c+=(math.factorial(digit))
            N=N//10
        if c==original:
            return 1
        return 0
