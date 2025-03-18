# https://leetcode.com/problems/minimum-size-subarray-sum/?envType=study-plan-v2&envId=top-interview-150

from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        result = 99999999999
        cur_sum = 0
        for i in range(len(nums)):
            cur_sum += nums[i]
            if cur_sum < target:
                continue
            
            while cur_sum >= target:
                result = min(result, i - l + 1)
                cur_sum -= nums[l]
                l += 1
        if result == 99999999999:
            return 0
        return result

target = 7
nums = [2, 3, 1, 2, 4, 3]

target = 4
nums = [1,4,4]

target = 11
nums = [1,1,1,1,1,1,1,1]

target = 213
nums = [12,28,83,4,25,26,25,2,25,25,25,12]
print(Solution().minSubArrayLen(target, nums))

