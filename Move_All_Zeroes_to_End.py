#User function Template for python3

class Solution:
	def pushZerosToEnd(self,arr):
    	# code here
    	count=0
    	for i in range(len(arr)):
    	    if arr[i]!=0:
    	        arr[i],arr[count]=arr[count],arr[i]
    	        count+=1
    	    
