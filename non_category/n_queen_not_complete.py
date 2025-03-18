# https://leetcode.com/problems/n-queens/

import copy

from typing import List

class Solution:
    def is_valid(self, matrix: List[List[str]]):
        for i, _ in enumerate(matrix):
            for j, _ in enumerate(matrix):
                if matrix[i][j] == 'Q':
                    cur_i, cur_j = i - 1, j - 1
                    while cur_i >= 0 and cur_i < len(matrix) and cur_j >= 0 and cur_j < len(matrix):
                        if matrix[cur_i][cur_j] == 'Q':
                            return False

                        cur_i -= 1
                        cur_j -= 1

                    cur_i, cur_j = i + 1, j + 1
                    while cur_i >= 0 and cur_i < len(matrix) and cur_j >= 0 and cur_j < len(matrix):
                        if matrix[cur_i][cur_j] == 'Q':
                            return False
                        
                        cur_i += 1
                        cur_j += 1

                    cur_i, cur_j = i + 1, j - 1
                    while cur_i >= 0 and cur_i < len(matrix) and cur_j >= 0 and cur_j < len(matrix):
                        if matrix[cur_i][cur_j] == 'Q':
                            return False
                        
                        cur_i += 1
                        cur_j -= 1
                    
                    cur_i, cur_j = i - 1, j + 1
                    while cur_i >= 0 and cur_i < len(matrix) and cur_j >= 0 and cur_j < len(matrix):
                        if matrix[cur_i][cur_j] == 'Q':
                            return False
                        
                        cur_i -= 1
                        cur_j += 1

                    cur_i, cur_j = i - 1, j
                    while cur_i >= 0 and cur_i < len(matrix) and cur_j >= 0 and cur_j < len(matrix):
                        if matrix[cur_i][cur_j] == 'Q':
                            return False
                        
                        cur_i -= 1
                    
                    cur_i, cur_j = i + 1, j
                    while cur_i >= 0 and cur_i < len(matrix) and cur_j >= 0 and cur_j < len(matrix):
                        if matrix[cur_i][cur_j] == 'Q':
                            return False
                        
                        cur_i += 1
        
        return True
  
    def solveNQueens(self, n: int) -> List[List[str]]:
        l_result = []
        def solution(matrix: List[List[int]], cursor_i: int):
            if cursor_i >= len(matrix):
                return
            
            if cursor_i == len(matrix) - 1 and self.is_valid(matrix):
                cur_line = []
                for i in range(len(matrix)):
                    cur_line.append(''.join(matrix[i]))
                
                l_result.append(cur_line[:])
                return

            for j in range(len(matrix)):
                matrix[cursor_i + 1][j] = 'Q'
                if self.is_valid(matrix):
                    solution(matrix, cursor_i + 1)

                matrix[cursor_i + 1][j] = '.'

            return

        matrix = []
        for i in range(n):
            matrix.append(['.'] * n)
        
        solution(matrix, -1)
        
        return l_result

# print(Solution().is_valid(
#     [
#         ['.', 'Q', '.', '.'],
#         ['.', '.', '.', 'Q'],
#         ['Q', '.', '.', '.'],
#         ['.', '.', 'Q', '.']
# ]))

# print(Solution().is_valid([["Q"]]))

print(Solution().solveNQueens(4))