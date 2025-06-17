#User function Template for python3

class Solution:
    def isPalindrome(self, n):
		# Code here
		original=n
		reverse=0
		while n>0:
		    reverse = reverse*10+(n%10)
		    n=n//10
		if reverse==original:
		    return True
        return False
		 
