from collections import Counter
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        freq = Counter(nums)
        for i in freq:
            if freq[i]==1:
                return i
