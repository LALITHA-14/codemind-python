#User function Template for python3
class Solution:
    def findIndex (self,arr, key ):
        #code here.
        if key not in arr:
            return [-1,-1]
        start=-1
        end=-1
        for i in range(len(arr)):
            if arr[i]==key:
                if start==-1:
                    start=i
                end=i
        return [start,end]
