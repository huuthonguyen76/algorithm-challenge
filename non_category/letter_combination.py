# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def solution(digits: str, solution_length: int, cur_txt: str, l_solution: List[str]):
            d_letter = {
                '2': ['a', 'b', 'c'],
                '3': ['d', 'e', 'f'],
                '4': ['g', 'h', 'i'],
                '5': ['j', 'k', 'l'],
                '6': ['m', 'n', 'o'],
                '7': ['p', 'q', 'r', 's'],
                '8': ['t', 'u', 'v'],
                '9': ['w', 'x', 'y', 'z']
            }

            if len(digits) == 0:
                if len(cur_txt) == solution_length:
                    l_solution.append(cur_txt)

                return l_solution

            for idx, digit in enumerate(digits):
                if digit == '':
                    continue

                for letter in d_letter[digit]:
                    l_solution = solution(digits=digits[idx + 1:], solution_length=solution_length, cur_txt=cur_txt + letter, l_solution=l_solution)

            return l_solution

        if len(digits) == 0:
            return []

        return solution(digits, len(digits), '', [])

print(Solution().letterCombinations(''))
