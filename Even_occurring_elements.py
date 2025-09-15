from collections import Counter
class Solution:
    def findEvenOccurrences(self, arr):
        # code here
        lst=[]
        freq=Counter(arr)
        for i in freq:
            if freq[i]%2==0 and i not in lst:
                lst.append(i)
        if not lst:
            return [-1]
        return lst
