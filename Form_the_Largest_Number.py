class Solution:

	def findLargest(self, arr):
	    # code here
	    arr=list(map(str,arr))
	    arr.sort(key=lambda x:x*10,reverse=True)
	    result=''.join(arr)
	    return result if result[0]!='0' else '0'
