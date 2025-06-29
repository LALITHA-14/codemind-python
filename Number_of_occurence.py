from collections import Counter
class Solution:
    def countFreq(self, arr, target):
        #code here
        freq = Counter(arr)
        return freq[target]
