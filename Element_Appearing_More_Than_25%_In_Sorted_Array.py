from collections import Counter
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        freq=Counter(arr)
        length=len(arr)//4
        for i in freq:
            if freq[i]>length:
                return i
