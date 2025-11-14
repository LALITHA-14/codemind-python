#User function Template for python3

class Solution:
    def getMinDiff(self, arr,k):
        # code here
        n=len(arr)
        arr.sort()
        ans=arr[n-1]-arr[0]
        for i in range(1,len(arr)):
            if arr[i]-k<0:
                continue
            min_elem=min(arr[0]+k,arr[i]-k)
            max_elem=max(arr[i-1]+k,arr[n-1]-k)
            ans=min(ans,max_elem-min_elem)
        return ans
