#User function Template for python3
class Solution:

	# Function to find maximum
	# product subarray
	def maxProduct(self,arr):
		                  # code here
		                  currmax=arr[0]
		                  currmin=arr[0]
		                  maxprod=arr[0]
		                  for i in range(1,len(arr)):
		                      temp=max(arr[i],currmax*arr[i],currmin*arr[i])
		                      currmin=min(arr[i],currmax*arr[i],currmin*arr[i])
		                      currmax=temp
		                      maxprod=max(maxprod,currmax)
		                  return maxprod

