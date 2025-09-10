from collections import Counter
from typing import List
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq=Counter(nums)
        max_values=max(freq.values())
        return sum(i for i in freq.values() if i==max_values)
