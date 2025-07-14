#User function Template for python3
class Solution:
	def removeDups(self, str):
		# code here
		first_occurence = ''.join(dict.fromkeys(s))
		return first_occurence
