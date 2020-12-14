"""
https://leetcode.com/problems/jewels-and-stones/
Thought process - Problem is similar to last problem(CountConsistentString, to check if character is in string
"""

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count = 0
        jewels = set(J)
        for letter in S:
            if letter in jewels:
                count += 1
        return count