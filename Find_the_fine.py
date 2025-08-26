#User function Template for python3

class Solution:
    def totalFine(self, date, car, fine):
        #Code here
        o=0
        e=0
        combine=list(zip(car,fine))
        if date%2==0:
            for i in range(len(combine)):
                if car[i]%2==1:
                    o+=fine[i]
            return o
        else:
            for i in range(len(combine)):
                if car[i]%2==0:
                    e+=fine[i]
            return e
        
    
    
