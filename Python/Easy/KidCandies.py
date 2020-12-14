# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        Output = []
        for candy in candies:
            if candy + extraCandies >= max(candies):
                Output.append(True)
            else:
                Output.append(False)
        return Output

# Trying to do list comprehension practice
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = max(candies)
        return [candy + extraCandies >= maxCandies for candy in candies]

