#User function Template for python3

class Solution:
    def armstrongNumber (self, n):
        # code here 
        av=n
        a=0
        while(n!=0):
            digit=n%10
            a+=digit**3
            n=n//10
        if av==a:
            return True
        return False
