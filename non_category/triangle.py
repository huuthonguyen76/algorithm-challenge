# https://leetcode.com/problems/triangle/

from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i, _ in enumerate(triangle):
            if i == 0:
                continue

            for j, _ in enumerate(triangle[i]):
                if j == 0:
                    triangle[i][j] += triangle[i - 1][j]
                else:
                    if j >= len(triangle[i]) - 1:
                        triangle[i][j] += triangle[i - 1][j - 1]
                    else:
                        triangle[i][j] += min(triangle[i - 1][j], triangle[i - 1][j - 1])
        
        return min(triangle[-1])


test_case_1 = ([[2],[3,4],[6,5,7],[4,1,8,3]], 11)

for test_case in [test_case_1]:
    if Solution().minimumTotal(test_case[0]) == test_case[1]:
        print("Pass")