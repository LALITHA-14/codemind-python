#User function Template for python3

class Solution:
	def findSum(self, n):
		# Code here
		even_count=n//2
		odd_count=n-even_count
		e=even_count*(even_count+1)
		o=odd_count*odd_count
	    return o,e
