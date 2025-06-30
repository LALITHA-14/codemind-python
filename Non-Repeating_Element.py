#User function Template for python3
from collections import Counter
class Solution:
    def firstNonRepeating(self, arr): 
        # Complete the function
        freq = Counter(arr)
        for i in freq:
            if freq[i]==1:
                return i
        return 0
