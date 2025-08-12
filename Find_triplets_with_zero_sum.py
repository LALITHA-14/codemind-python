class Solution:
    def findTriplets(self, arr):
        #code here
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                for k in range(j+1,len(arr)):
                    if arr[i]+arr[j]+arr[k]==0:
                        return True
        return False
