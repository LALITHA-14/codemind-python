import math
class Solution:
    def nCr(self, n, r):
        # code here
        number = math.factorial(n)
        if n>=r: 
            fact = math.factorial(n-r)
            rand = math.factorial(r)
            final = (number)//(fact*rand)
            return final
        else:
            return 0
