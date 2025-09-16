class Solution:
	def twoSum(self, arr, target):
		# code here
		s=set()
		for i in arr:
		    if target-i in s:
		        return True
		    s.add(i)
		return False
