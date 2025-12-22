from datetime import date
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        da=date(year,month,day)
        return da.strftime("%A")
