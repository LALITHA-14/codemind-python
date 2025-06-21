import math
#User function Template for python3

class Solution:
    def lcmAndGcd(self, a : int, b : int) -> List[int]:
        # code here
        lst=[]
        lcm=math.lcm(a,b)
        gcd=math.gcd(a,b)
        return lcm,gcd
        
