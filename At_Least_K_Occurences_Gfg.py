from collections import Counter
class Solution:
    def firstElementKTime(self, arr,k):
        # code here
        freq=Counter(arr)
        count={}
        for i in arr:
            count[i]=count.get(i,0)+1
            if count[i]==k:
                return i
        return -1
