from collections import Counter
class Solution:
    def maxFreqSum(self, s: str) -> int:
        freq=Counter(s)
        vowels=set("aeiou")
        max_vo=0
        max_co=0
        for ch,count in freq.items():
            if ch in vowels:
                max_vo=max(count,max_vo)
            else:
                max_co=max(count,max_co)
        return max_vo+max_co
