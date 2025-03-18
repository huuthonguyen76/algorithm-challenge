# https://leetcode.com/problems/combination-sum/

from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        l_solution = []
        def solution(candidates: List[int], target: int, cursor: int, l_cur_result: List[int]) -> List[List[int]]:
            if sum(l_cur_result) == target:
                return 1

            if sum(l_cur_result) > target:
                return 0

            for cursor, _ in enumerate(candidates):
                is_good_solution = solution(candidates, target, cursor + 1, l_cur_result + [candidates[cursor]])
                l_temp_result = l_cur_result + [candidates[cursor]]
                if is_good_solution:
                    l_sorted_temp_result = l_temp_result[:]
                    l_sorted_temp_result = sorted(l_sorted_temp_result)

                    if l_sorted_temp_result not in l_solution:
                        l_solution.append(l_sorted_temp_result)

            return 0

        solution(candidates, target, 0, [])
        return l_solution

        

test_case_1 = (([2, 3, 6, 7], 7), 2)
test_case_2 = (([2, 3, 5], 8), 3)
test_case_3 = (([2], 1), 0)

for test_case in [test_case_1, test_case_2, test_case_3]:
    if len(Solution().combinationSum(test_case[0][0], test_case[0][1])) != test_case[1]:
        print("Wrong")