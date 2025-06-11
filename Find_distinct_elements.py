#User function Template for python3
def distinct(arr):
    # Your Code here
    distinct_elements=set(arr) # distinct elements are not repeatable elements in an array
    c=0
    for i in range(len(distinct_elements)):
        c+=1
    return c
