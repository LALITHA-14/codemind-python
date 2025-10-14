#User function Template for python3
class Solution:
	def reverseSubArray(self,arr,l,r):
		# code here
		start_index=l-1
		end_index=r-1
		left=start_index
		right=end_index
		while(left<right):
		    arr[left],arr[right]=arr[right],arr[left]
		    left+=1
		    right-=1
	    return arr
