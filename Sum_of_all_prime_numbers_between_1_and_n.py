class Solution:
    def isprime(self,num):
        if num<=1:
            return False
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                return False
        return True
    def prime_Sum(self, n):
        # Code here
        lst=[]
        for i in range(1,n+1):
            if self.isprime(i):
                lst.append(i)
        return sum(lst)
