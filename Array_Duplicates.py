class Solution:
    def findDuplicates(self, arr):
        # code here
        arr.sort()
        duplicates = []
        for i in range(1, len(arr)):
            if arr[i]==arr[i-1] and (not duplicates or duplicates[-1]!=arr[i]):
                duplicates.append(arr[i])
        return duplicates
        
