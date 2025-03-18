# https://leetcode.com/problems/permutations-ii/

from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        l_solution = []
        def solution(nums: List[int], l_cur_result: List[int], l_avoid_idx: List[int]):
            # if l_cur_result in l_solution:
            #     return

            if len(l_cur_result) == len(nums):
                l_solution.append(l_cur_result[:])
                return

            for idx, num in enumerate(nums):
                if idx in l_avoid_idx:
                    continue

                solution(nums=nums, l_cur_result=l_cur_result + [num], l_avoid_idx=l_avoid_idx + [idx])

        solution(nums=nums, l_cur_result=[], l_avoid_idx=[])
        return l_solution

print(Solution().permuteUnique([1, 1, 2]))
