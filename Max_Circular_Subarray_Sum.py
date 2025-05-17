#User function Template for python3

#Complete this function
#Function to find maximum circular subarray sum.
def circularSubarraySum(arr):
    ##Your code here
    totalsum=0
    minsum=arr[0]
    maxsum=arr[0]
    currmax=0
    currmin=0
    for i in range(len(arr)):
        currmax=max(arr[i],currmax+arr[i])
        maxsum=max(maxsum,currmax)
        currmin=min(arr[i],currmin+arr[i])
        minsum=min(minsum,currmin)
        totalsum+=arr[i]
    normalsum=maxsum
    circularsum=totalsum-minsum
    if minsum==totalsum:
        return normalsum
    return max(normalsum,circularsum)
        

