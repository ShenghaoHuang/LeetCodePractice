class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        values = []
        for total in accounts:
            values.append(sum(total))
        return max(values)