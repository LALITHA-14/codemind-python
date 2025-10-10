#User function Template for python3
class Solution:
	def matSearch(self, mat, x):
		# Complete this function
		found=any(x in row for row in matrix)
		return found
