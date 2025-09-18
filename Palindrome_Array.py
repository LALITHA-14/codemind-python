
from typing import List


class Solution:
    def isPerfect(self, arr : List[int]) -> bool:
        # code here
        a=[]
        for i in reversed(arr):
            a.append(i)
        if a==arr:
            return True
        else:
            return False
