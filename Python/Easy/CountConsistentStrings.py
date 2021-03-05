"""
https://leetcode.com/problems/count-the-number-of-consistent-strings/
First solution was to create a list but then someone showed me instead of using a list
to use a set for faster run time.
"""

class Solution:
    def countConsistentStrings(self, allowed: str, words) -> int:
        allowed_count = len(words)
        #letters = [letter for letter in allowed]
        letters = set(allowed)
        for word in words:
            for letter in word:
                if letter not in letters:
                    allowed_count -= 1
                    break
        return allowed_count
