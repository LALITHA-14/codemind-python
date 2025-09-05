#User function Template for python3
class Solution:
	def firstAlphabet(self, S):
		# code here
		word=S.split()
		result="".join([w[0] for w in word])
		return result
