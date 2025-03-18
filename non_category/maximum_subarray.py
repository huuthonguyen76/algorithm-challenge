# https://leetcode.com/problems/maximum-subarray/

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_val = -999999
        cur_val = 0
        for num in nums:
            cur_val += num
            
            if cur_val < num:
                cur_val = num
            
            max_val = max(max_val, cur_val)
        
        return max_val
        

test_case_1 = ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6)
test_case_2 = ([1], 1)
test_case_3 = ([5, 4, -1, 7, 8], 23)

for test_case in [test_case_1, test_case_2, test_case_3]:
    if Solution().maxSubArray(test_case[0]) != test_case[1]:
        print("Wrong")
