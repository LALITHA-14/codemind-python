#User function Template for python3
class Solution:
    def getMoreAndLess(self, arr, target):
		# code here
		c=0
		s=0
		for i in range(len(arr)):
		    if arr[i]<=target:
		        c+=1
		    if arr[i]>=target:
		        s+=1
		return c,s
