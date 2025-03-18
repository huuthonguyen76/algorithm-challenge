# https://leetcode.com/problems/rotate-array/?envType=study-plan-v2&envId=top-interview-150

from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        if k == 0:
            return

        l_new_arr = nums[len(nums) - k:len(nums)][:] + nums[:len(nums) - k][:]
        print(l_new_arr)
        
        for idx in range(len(nums)):
            nums[idx] = l_new_arr[idx]


Solution().rotate([1,2,3,4,5,6,7], 3)
