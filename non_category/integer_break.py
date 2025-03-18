# https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/

from typing import List


class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        
        mid = nums[len(nums)//2]
        result = 0
        for i in nums:
            result+=abs(mid-i)
        
        return result
        

test_case_1 = ([1,0,0,8,6], 14)
for test_case in [test_case_1]:
    if Solution().minMoves2(test_case[0]) != test_case[1]:
        print('Fail', test_case)

