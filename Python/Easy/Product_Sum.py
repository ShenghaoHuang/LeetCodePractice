"""
https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/
"""
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n_list = [int(x) for x in str(n)]
        product = 1
        sum = 0
        for x in n_list:
            product *= x
        for x in n_list:
            sum += x
        return product-sum
