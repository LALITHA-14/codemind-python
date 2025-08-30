from itertools import combinations
from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result=set()
        for r in range(len(nums)+1):
            for comb in combinations(nums,r):
                result.add(comb)
        return [subset for subset in sorted(result)]
