def pos(n):
    ## Write the code
    if n>0:
        for i in reversed(range(0,n)):
            print(i,end=" ")
    
def neg(n):
    ##Write the code
    if n<0:
        for i in range(n,1):
            print(i,end=" ")
