class Solution:
    def findExtra(self,a,b):
        #add code here
        low=0
        high=len(arr2)-1
        while(low<=high):
            mid=(low+high)//2
            if arr1[mid]==arr2[mid]:
                low=mid+1
            else:
                high=mid-1
        return low
