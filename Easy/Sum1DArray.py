# class Solution:
#     def runningSum(self, nums: List[int]) -> List[int]:
#         value = []
#         value_sum = []
#         for num in nums:
#             value.append(num)
#             value_sum.append(sum(value))
#         return value_sum


#Faster solution run time
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        value_sum = []
        value = 0
        for num in nums:
            value += num
            value_sum.append(value)
        return value_sum