# https://leetcode.com/problems/largest-number/

import functools

from typing import List

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(x, y):
            if x + y > y + x:
                return 1
            else:
                return -1

        l_txt = [str(ele) for ele in nums]
        l_sorted_txt = sorted(l_txt, key=functools.cmp_to_key(compare))
        
        l_sorted_txt = l_sorted_txt[::-1]

        return int(''.join(l_sorted_txt))
        
print(Solution().largestNumber([3,30,34,5,9]))