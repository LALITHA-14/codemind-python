class Solution:
	def isPalindrome(self, S):
		# code here
		a = S[::-1]
		if(a==S):
		    return 1
		return 0

