import math
class Solution:
    def isPerfect(self, n):
        # code here 
        c=1
        if n==1:
            return False # 1 is not a Perfect Number
        for i in range(2,int(math.sqrt(n))+1):
            if n%i==0:
                c+=i
                if i!=n//i:
                    c+=n//i # Avoiding square root twice
        return c==n
