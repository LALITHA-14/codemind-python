import math
class Solution:
    def reverse_exponentiation(self, n):
        # code here
        original= n
        rev=0
        while n>0:
            rev=rev*10+(n%10)
            n=n//10
        return pow(original,rev)
