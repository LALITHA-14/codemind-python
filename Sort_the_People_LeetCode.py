from typing import List
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        people=list(zip(heights,names))
        people.sort(reverse=True)
        return [name for _,name in people]
