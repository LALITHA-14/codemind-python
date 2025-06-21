import math
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        a = int(math.sqrt(num))
        b=a*a
        if b==num:
            return True
        return False
        

        
