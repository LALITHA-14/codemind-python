class Solution:
    def longest(self, arr):
        # code here
        maximum=0
        longest=""
        for i in arr:
            if len(i)>maximum:
                maximum=len(i)
                longest=i
        return longest
