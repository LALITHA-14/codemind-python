class Solution:
    def intersection(self, arr1, arr2):
        #code here
        a1=set(arr1)
        a2=set(arr2)
        return list(sorted(a1.intersection(a2)))
