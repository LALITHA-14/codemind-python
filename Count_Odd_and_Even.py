class Solution:
	def countOddEven(self, arr):
		#Code here
		e=0
		o=0
		for i in range(len(arr)):
		    if arr[i]%2==0:
		        e+=1
		    else:
		        o+=1
	    return o,e
