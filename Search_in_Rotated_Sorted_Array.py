class Solution:
    def search(self, arr, key):
        # code here
        for i in range(0,len(arr)):
            if arr[i]==key:
                return i
        return -1
        
