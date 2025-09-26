class Solution:
    def sumOfDigits(self, n):
        # code here
        lst=[]
        while(n>0):
            r=n%10
            lst.append(r)
            n=n//10
        return sum(lst)
