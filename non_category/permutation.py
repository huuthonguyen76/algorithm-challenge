# https://leetcode.com/problems/permutations/

from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        l_result = []
        def solution(nums: List[int], l_cur_result: List[int]):
            if len(nums) == len(l_cur_result):
                l_result.append(l_cur_result[:])
                return

            for num in nums:
                if num in l_cur_result:
                    continue

                solution(nums=nums, l_cur_result=l_cur_result + [num])
        
        solution(nums, [])
        return l_result
                

print(Solution().permute([1, 2, 3]))
