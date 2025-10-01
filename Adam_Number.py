#User function Template for python3

class Solution:
    def checkAdamOrNot(self, N):
        # code here 
        s=N*N
        rev=0
        while(N!=0):
            r=N%10
            rev=(rev*10)+r
            N=N//10
        a=rev*rev
        av=a
        rs=0
        while(a!=0):
            p=a%10
            rs=(rs*10)+p
            a=a//10
        if s==rs:
            return "YES"
        else:
            return "NO"
