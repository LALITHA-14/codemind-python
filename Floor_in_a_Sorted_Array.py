class Solution:
    #User function Template for python3
    
    #Complete this function
    def findFloor(self, arr, x):
        #Your code here
        last=-1
        for i in range(len(arr)):
            if arr[i]<=x:
                last=i
        return last
        
