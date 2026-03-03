class Solution:
    def average(self, salary: List[int]) -> float:
        salary.remove(max(salary))
        salary.remove(min(salary))
        mean=sum(salary)/len(salary)
        return round(mean,5)
