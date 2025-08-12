class Solution:
    def hasTripletSum(self, arr, target):
        # Code Here
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                for k in range(j+1,len(arr)):
                    if arr[i]+arr[j]+arr[k]==target:
                        return True
        return False
