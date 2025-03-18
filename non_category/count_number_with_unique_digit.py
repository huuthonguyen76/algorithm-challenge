# Reference: https://leetcode.com/problems/non-decreasing-subsequences/

from collections import Counter
from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        l_result = []
        l_num = nums

        def recur(l_cur_result, cur_idx, d_potential):
            if len(l_cur_result) >= 2 and l_cur_result not in l_result:
                l_result.append(l_cur_result)

            if len(d_potential[cur_idx]) == 0:
                return

            for ele in d_potential[cur_idx]:
                recur(l_cur_result + [l_num[ele]], ele, d_potential)

        d_potential = {}
        for idx, num in enumerate(l_num):
            d_potential[idx] = []

            for idx_2, num_2 in enumerate(l_num):
                if idx_2 <= idx:
                    continue
                if num <= num_2:
                    d_potential[idx].append(idx_2)

        for idx, num in enumerate(l_num):
            recur([l_num[idx]], idx, d_potential)

        return l_result

test_case_1 = ([4,6,7,7], 8)
for test_case in [test_case_1]:
    if len(Solution().findSubsequences(test_case[0])) != test_case[1]:
        print("Failed: ", test_case[0], test_case[1])
