import re
class Solution:
	def isPalinSent(self, s):
		# code here
		res=re.sub(r'[^a-zA-Z0-9]','',s).lower()
		rev=res[::-1]
		return rev==res
