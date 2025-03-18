# https://leetcode.com/problems/subsets/description/?envType=problem-list-v2&envId=backtracking

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.result = []

        def recursive(l_num: List[int], l_cur_num: List[int]):
            # if l_cur_num[:] not in self.result:
            self.result.append(l_cur_num[:])
            
            for i, ele in enumerate(l_num):
                recursive(l_num=l_num[i+1:], l_cur_num=l_cur_num + [ele])

        recursive(nums, [])
        return self.result
            
        

print(Solution().subsets([1, 2, 3]))