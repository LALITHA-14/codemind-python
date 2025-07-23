#User function Template for python3

def Search(arr,n,k):
    #code here
    for i in range(0,len(arr)):
        if arr[i]==k:
            return i
    return -1
