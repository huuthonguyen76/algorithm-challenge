# https://leetcode.com/problems/house-robber/

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums)
        
        if len(nums) == 3:
            return max(nums[0] + nums[2], nums[1])
        
        l_dp = [0] * len(nums)
        l_dp[0] = nums[0]
        l_dp[1] = max(nums[0], nums[1])
        l_dp[2] = nums[0] + nums[2]
        
        for i, _ in enumerate(l_dp):
            if i <= 2:
                continue

            l_dp[i] = nums[i] + max(l_dp[i - 2], l_dp[i - 3])
        
        return max(l_dp)
            


test_case_1 = ([1,2,3,1], 4)
test_case_2 = ([2,7,9,3,1], 12)
for test_case in [test_case_1, test_case_2]:
# for test_case in [test_case_2]:
    if Solution().rob(test_case[0]) != test_case[1]:
        print("Not Pass", test_case)