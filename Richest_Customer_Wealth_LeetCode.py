class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        result = [sum(row) for row in accounts]
        return max(result)
