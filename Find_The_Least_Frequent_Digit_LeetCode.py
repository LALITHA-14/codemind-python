from collections import Counter
class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        lst=[]
        lst.extend([int(digits) for digits in str(n)])
        freq=Counter(lst)
        min_freq=min(freq.values())
        least_digits=([d for d in freq if freq[d]==min_freq])
        return min(least_digits)
