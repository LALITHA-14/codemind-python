#User function Template for python3
import re
class Solution:
	def sentencePalindrome(self, s):
		# your code here
		new_string = re.sub(r'[^a-zA-Z0-9]','',s).lower()
		reversed_string = new_string[::-1]
		if new_string==reversed_string:
		    return True
		return False
