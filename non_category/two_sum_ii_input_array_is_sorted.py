# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/?envType=study-plan-v2&envId=top-interview-150

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while True:
            if numbers[l] + numbers[r] > target:
                r -= 1
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                return [l + 1, r + 1]

test_case_1 = (([2,7,11,15], 9), [1, 2])
for test_case in [test_case_1]:
    print(Solution().twoSum(test_case[0][0], test_case[0][1]))
    print(Solution().twoSum(test_case[0][0], test_case[0][1]) == test_case[1])
