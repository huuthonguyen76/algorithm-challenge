# https://leetcode.com/problems/maximum-product-subarray/

from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        upper, lower = 1, 1
        result = float('-inf')
        for i, num in enumerate(nums):
            result = max(num, num * upper, num * lower, result)
            upper, lower = max(num, num * upper, num * lower), min(num, num * upper, num * lower)

        return result

# hunta-957

test_case_1 = ([2, 3, -2, 4], 6)
test_case_2 = ([-2, 0, -1], 0)
test_case_3 = ([-2, 3, -4], 24)
test_case_4 = ([0, 2], 2)

# test_case_1 = ([2, 3, -2, 3, -1, 0, 2, -1], 36)
# test_case_1 = ([2,-5,-2, 2, 1, -4, 3], 48)
test_case_1 = ([2, -5, 2, 2], 4)
for test_case in [test_case_1, test_case_2, test_case_3, test_case_4]:
# for test_case in [test_case_2]:
    if Solution().maxProduct(test_case[0]) != test_case[1]:
        print("Not Pass", test_case)