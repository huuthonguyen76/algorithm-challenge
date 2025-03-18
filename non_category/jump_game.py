# https://leetcode.com/problems/jump-game/?envType=problem-list-v2&envId=dynamic-programming

from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        gas = 0
        
        for num in nums:
            print(num, gas)
            if gas < 0:
                return False
            elif num >= gas:
                gas = num
            gas -= 1

        return True


Solution().canJump([2,0,0])
