# https://leetcode.com/problems/unique-paths-ii/?envType=problem-list-v2&envId=dynamic-programming

from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0

        new_matrix = [
            [0] * len(obstacleGrid[0]) for ele in obstacleGrid
        ]
        new_matrix[0][0] = 1
    
        for i in range(len(new_matrix)):
            for j in range(len(new_matrix[0])):
                if obstacleGrid[i][j] == 1:
                    new_matrix[i][j] = 0
                    continue

                if i == 0:
                    if j == 0:
                        continue
                    else:
                        new_matrix[i][j] = new_matrix[i][j - 1]
                    continue

                if j == 0:
                    new_matrix[i][j] = new_matrix[i - 1][j]
                else:
                    top  = new_matrix[i - 1][j]
                    left = new_matrix[i][j - 1]
                    new_matrix[i][j] = top + left

        return new_matrix[-1][-1]

obstacleGrid = [
    [0, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 0]
]
obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
obstacleGrid = [[0,1,0,0]]
print(Solution().uniquePathsWithObstacles(obstacleGrid))