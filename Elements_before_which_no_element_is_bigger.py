class Solution:
    def count_elements(self, arr):
        # code here
        c=0
        max_so_far=float('-inf')
        for i in arr:
            if i>max_so_far:
                c+=1
                max_so_far=i
        return c
