#User function Template for python3

class Solution:
	def is_AutomorphicNumber(self, n):
		# Code here
		a=str(n*n)
		s=str(n%10)
		if a.endswith(s):
		    return "Automorphic"
		else:
		    return "Not Automorphic"
