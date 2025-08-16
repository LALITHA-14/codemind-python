from collections import Counter
class Solution:
    def nonRepeatingChar(self,s):
        #code here
        freq=Counter(s)
        for i in freq:
            if freq[i]==1:
                return i
        return -1
    
