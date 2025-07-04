#User function Template for python3

class Solution:
    #Function to return list containing first n fibonacci numbers.
    def fibonacciNumbers(self,n):
        # your code here
        fib=[]
        a,b=0,1
        for i in range(n):
            fib.append(a)
            a,b=b,a+b
        return fib
