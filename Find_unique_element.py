from collections import Counter
class Solution:
    def find_unique(self, k, arr):
        #code here
        freq=Counter(arr)
        for i in freq:
            if freq[i]!=k:
                return i
