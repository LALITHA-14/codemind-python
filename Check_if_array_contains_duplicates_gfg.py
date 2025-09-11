from collections import Counter
class Solution:

    def checkDuplicates(self, arr):
        #code here
        freq=Counter(arr)
        for i in freq:
            if freq[i]>1:
                return True
        return False
