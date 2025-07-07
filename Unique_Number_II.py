#User function Template for python3
from collections import Counter
class Solution:
	def singleNum(self, arr):
		# Code here
		lst=[]
        freq = Counter(arr)
        for i in freq:
            if freq[i]==1:
                lst.append(i)
        return min(lst),max(lst)
