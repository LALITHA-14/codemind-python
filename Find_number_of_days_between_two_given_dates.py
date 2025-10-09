#User function Template for python3
from datetime import date
class Solution:
    def noOfDays(self, d1, m1, y1, d2, m2, y2):
        # code here 
        date1=date(y1,m1,d1)
        date2=date(y2,m2,d2)
        return abs((date2-date1).days)
