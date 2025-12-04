class Solution:
	def countTriplet(self, arr):
		# code here
		arr.sort()
		n=len(arr)
		count=0
		for k in range(n-1,-1,-1):
		    i=0
		    j=k-1
		    while i<j:
		        if arr[i]+arr[j]==arr[k]:
		            count+=1
		            i+=1
		            j-=1
		        elif arr[i]+arr[j]<arr[k]:
		            i+=1
		        else:
		            j-=1
	    return count
