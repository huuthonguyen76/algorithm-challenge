# https://leetcode.com/problems/combination-sum/

from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        l_solution = []
        d_tracking = {}
        
        def get_key(l_num: List[int]):
            txt = ''
            for num in l_num:
                txt += str(num) + ' '            
            return txt

        def solution(candidates: List[int], target: int, l_cur_result: List[int]) -> List[List[int]]:
            if sum(l_cur_result) == target:
                return 1

            if sum(l_cur_result) > target:
                return 0
            
            if len(candidates) == 0:
                return 0

            cur_key = get_key(l_cur_result)
            if cur_key in d_tracking:
                return 0
            
            d_tracking[cur_key] = True
            
            for cursor, val in enumerate(candidates):
                is_good_solution = solution(candidates[cursor + 1:], target, l_cur_result + [val])
                l_temp_result = l_cur_result + [val]
                if is_good_solution:
                    l_sorted_temp_result = l_temp_result[:]
                    # l_sorted_temp_result = sorted(l_sorted_temp_result)

                    if l_sorted_temp_result not in l_solution:
                        l_solution.append(l_sorted_temp_result)

            return 0

        candidates.sort()
        
        solution(candidates, target, [])
        # print(l_solution)
        return l_solution

        

test_case_1 = (([10,1,2,7,6,1,5], 8), 4)
test_case_2 = (([2,5,2,1,2], 5), 2)

for test_case in [test_case_1, test_case_2]:
    if len(Solution().combinationSum2(test_case[0][0], test_case[0][1])) != test_case[1]:
        print("Wrong")