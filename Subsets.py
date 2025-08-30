#User function Template for python3
from itertools import combinations
from typing import List
class Solution:
    def subsets(self, arr):
        # code here
        arr.sort()
        result=set()
        for r in range(len(arr)+1):
            for comb in combinations(arr,r):
                result.add(comb)
        return [subset for subset in sorted(result)]
