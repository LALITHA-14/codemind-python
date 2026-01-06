from collections import Counter
class Solution:
    def maxDifference(self, s: str) -> int:
        freq=Counter(s)
        odd_max=float('-inf')
        even_min=float('inf')
        for i in freq.values():
            if i%2==1:
                odd_max=max(odd_max,i)
            else:
                even_min=min(even_min,i)
        return odd_max-even_min
