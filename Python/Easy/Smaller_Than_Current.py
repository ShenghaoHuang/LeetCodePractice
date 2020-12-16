"""
https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
"""
#My answer is the first one, I started comparing and checking other answers to see where I could improve
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count = 0
        value = []
        for x in nums:
            for y in nums:
                if x > y:
                    count += 1
            value.append(count)
            count = count * 0
        return value

#This solution was one I saw online that's runtime was a lot faster than my solution.
#I thought it was a really good solution that seemed elegant
# class Solution:
#     def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
#         nums_sort = sorted(nums)
#         values = {}
#         result = []
#         for x in range(len(nums)):
#             if nums_sort[x] not in values:
#                 values[nums_sort[x]] = x
#         for x in range(len(nums)):
#             result.append(values[nums[x]])
#         return result