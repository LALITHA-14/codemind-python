class Solution:
    def sumOfDivisors(self, n):
    	#code here 
    	s=0
    	for i in range(1,n+1):
    	    s+=i*(n//i)
    	return s
