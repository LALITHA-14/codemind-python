from collections import Counter
class Solution:
    def findMajority(self, arr):
        # code here
        floors=len(arr)//3
        freq=Counter(arr)
        lst=[]
        for i in freq:
            if freq[i]>floors:
                lst.append(i)
        return sorted(lst)
