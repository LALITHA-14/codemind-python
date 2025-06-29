#User function Template for python3
from collections import Counter
class Solution:
    
    def getSingle(self,arr):
        # code here
        freq = Counter(arr)
        for i in arr:
            if freq[i]%2!=0:
                return i
