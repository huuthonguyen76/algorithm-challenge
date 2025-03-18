# https://leetcode.com/problems/minimum-path-sum/

from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        for j in range(1, len(grid[0])):
            grid[0][j] = grid[0][j - 1] + grid[0][j]
        
        for i in range(1, len(grid)):
            grid[i][0] = grid[i][0] + grid[i - 1][0]
            
        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]

        return grid[-1][-1]

test_case_1 = ([[1,3,1],[1,5,1],[4,2,1]], 7)
for test_case in [test_case_1]:
    if Solution().minPathSum(test_case[0]) != test_case[1]:
        print("Wrong")
