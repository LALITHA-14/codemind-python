from collections import Counter
class Solution:
    #Function to find all elements in array that appear more than n/k times.
    def countOccurence(self,arr, k):
        #Your code here
        freq = Counter(arr)
        count=0
        n=len(arr)
        occur=n//k
        for i in freq:
            if freq[i]>occur:
               count+=1
        return count
