from collections import Counter
class Solution:
    def moreFrequent(self, arr, x, y):
        #code here
        freq=Counter(arr)
        a = freq[x]
        b = freq[y]
        if a==b:
            return x if x<y else y
        return x if a>b else y
