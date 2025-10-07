from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq=Counter(s)
        for i,val in enumerate(s):
            if freq[val]==1:
                return i
        return -1
