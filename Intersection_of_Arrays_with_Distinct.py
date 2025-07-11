#User function Template for python3

#Function to return the count of the number of elements in
#the intersection of two arrays.
class Solution:
    def numberofElementsInIntersection(self,a, b):
        #return: expected length of the intersection array.
        #code here
        a1 = set(a)
        b1 = set(b)
        return len(a1.intersection(b1))
