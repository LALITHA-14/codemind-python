#User function Template for python3
import math
class Solution:
    def factorial(self, n):
        #code here
        fact=math.factorial(n)
        s=str(fact)
        lst=[]
        for i in s:
            lst.append(i)
        return lst
