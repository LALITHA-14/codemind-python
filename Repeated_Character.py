#User function Template for python3
from collections import Counter
class Solution:
    def firstRep(self, s):
        # code here
        freq=Counter(s)
        for i,val in enumerate(s):
            if freq[val]>1:
                return val
        return '#'
