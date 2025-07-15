class Solution:
    def divby13(self, s):
        # code here 
        # for 10^5 inputs this problem can be solved using modulo simulation method
        remainder = 0
        for digits in s:
            remainder = (remainder*10+int(digits))%13
        return remainder==0
