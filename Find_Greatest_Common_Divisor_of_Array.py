import math
class Solution:
    def findGCD(self, nums: List[int]) -> int:
       x=max(nums)
       y=min(nums)
       return math.gcd(x,y)
