"""
https://leetcode.com/problems/shuffle-string/
"""
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        repair = list(" " * len(s))
        for num in range(len(s)):
            repair[indices[num]] = s[num]
        return "".join(repair)