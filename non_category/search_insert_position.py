# https://leetcode.com/problems/search-insert-position/?envType=study-plan-v2&envId=top-interview-150

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def search_recursive(nums, target, left, right):
            if left > right:
                return left

            center = (left + right) // 2
            
            if nums[center] == target:
                return center
            elif nums[center] < target:
                return search_recursive(nums, target, center + 1, right)
            else:
                return search_recursive(nums, target, left, center - 1)
        
        return search_recursive(nums, target, 0, len(nums) - 1)


nums = [1,3,5,6]
target = 5

print(Solution().searchInsert(nums, target))

