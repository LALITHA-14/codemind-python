#User function Template for python3
class Solution:
	def addBinary(self, s1, s2):
		# code here
		a1=int(s1,2)
		b1=int(s2,2)
		return bin(a1+b1)[2:]
