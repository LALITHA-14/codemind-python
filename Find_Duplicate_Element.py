#User function Template for python3
from collections import Counter
class Solution:
    def findDuplicate(self,arr):
    # Your code goes here
        freq=Counter(arr)
        for i in freq:
            if freq[i]>1:
                return i





    
