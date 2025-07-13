#User function Template for python3

class Solution:
    
    #Function to return a list containing the union of the two arrays.
    def findUnion(self,a,b):
        # code here 
        lst=[]
        a1=set(a)
        b1=set(b)
        union_of_a_and_b = a1.union(b1)
        return sorted(union_of_a_and_b)
