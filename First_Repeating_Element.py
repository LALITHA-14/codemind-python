from collections import Counter
class Solution:
    def firstRepeated(self,arr):
        # code here 
        seen=set()
        freq=Counter(arr)
        for i,num in enumerate(arr,start=1):
            if freq[num]>1:
                return i
        return -1
