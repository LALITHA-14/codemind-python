#User function Template for python3
from collections import Counter
class Solution:
    def uniqueId(self, arr):
        #  code here
        freq=Counter(arr)
        lst=[]
        for i in freq:
            if freq[i]>=1:
                lst.append(i)
        return lst
