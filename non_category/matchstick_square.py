# https://leetcode.com/problems/matchsticks-to-square/description/

from typing import List


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        l_solution = [False]
        if sum(matchsticks) % 4 != 0:
            return False

        target = sum(matchsticks) / 4
        def solution(matchsticks: List[int], l_result: List[int]):
            if len(matchsticks) == 0:
                for ele in l_result:
                    if ele != target:
                        return

                l_solution[0] = True

            if l_solution[0]:
                return

            for idx_stick, stick in enumerate(matchsticks):
                for idx_result, _ in enumerate(l_result):
                    if l_result[idx_result] + stick <= target:
                        l_result[idx_result] += stick
                        solution(matchsticks = matchsticks[idx_stick + 1:], l_result=l_result)
                        l_result[idx_result] -= stick
        
        solution(matchsticks=matchsticks, l_result=[0, 0, 0, 0])
        
        return l_solution[0]


test_case_1 = ([1,1,2,2,2], True)
test_case_1 = ([3,3,3,3,4], False)
test_case_1 = ([5,5,5,5,4,4,4,4,3,3,3,3], True)
for test_case in [test_case_1]:
    if Solution().makesquare(test_case[0]) != test_case[1]:
        print("FAIL")

