from collections import Counter
class Solution:
    def frequencyCount(self, arr):
        #  code here
        freq=Counter(arr)
        n=len(arr)
        lst=[]
        for i in range(1,n+1):
            if i in freq:
                lst.append(freq[i])
            else:
                lst.append(0)
        return lst
