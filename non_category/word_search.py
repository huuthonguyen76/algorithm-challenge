# https://leetcode.com/problems/word-search/

import copy

from typing import List
from collections import Counter

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def add_border(board: List[List[str]]) -> List[List[str]]:
            new_board = []
            for _ in range(len(board) + 2):
                new_board.append(['.'] * (len(board[0]) + 2))

            for i in range(len(new_board)):
                for j in range(len(new_board[0])):
                    if i > 0 and i < len(new_board) - 1 and j > 0 and j < len(new_board[0]) - 1:
                        new_board[i][j] = board[i - 1][j - 1]
            
            return new_board


        def solution(cur_i: int, cur_j: int, board: List[List[int]], cur_path: str):
            if board[cur_i][cur_j] == '.' or word[len(cur_path) - 1] != cur_path[-1]:
                return False
            
            board[cur_i][cur_j] = '.'

            if cur_path == word:
                return True

            cur_board_character = board[cur_i + 1][cur_j]
            if solution(cur_i=cur_i + 1, cur_j=cur_j, board=board, cur_path=cur_path + board[cur_i + 1][cur_j]):
                return True

            board[cur_i + 1][cur_j] = cur_board_character
            
            cur_board_character = board[cur_i][cur_j + 1]
            if solution(cur_i=cur_i, cur_j=cur_j + 1, board=board, cur_path=cur_path + board[cur_i][cur_j + 1]):
                return True
            board[cur_i][cur_j + 1] = cur_board_character
            
            cur_board_character = board[cur_i - 1][cur_j]
            if solution(cur_i=cur_i - 1, cur_j=cur_j, board=board, cur_path=cur_path + board[cur_i - 1][cur_j]):
                return True
            board[cur_i - 1][cur_j] = cur_board_character
            
            cur_board_character = board[cur_i][cur_j - 1]
            if solution(cur_i=cur_i, cur_j=cur_j - 1, board=board, cur_path=cur_path + board[cur_i][cur_j - 1]):
                return True
            board[cur_i][cur_j - 1] = cur_board_character

            return False

        c_count_board = Counter()
        c_count_word = Counter()

        new_board = add_border(board)

        l_start_pos = []
        first_character = word[0]
        for i in range(len(new_board)):
            for j in range(len(new_board[0])):
                if new_board[i][j] == first_character:
                    l_start_pos.append((i, j))
                    
                c_count_board[new_board[i][j]] += 1

        for character in word:
            c_count_word[character] += 1

        for character in word:
            if c_count_word[character] > c_count_board[character]:
                return False

        for start_i, start_j in l_start_pos:
            if solution(start_i, start_j, copy.deepcopy(new_board), first_character) is True:
                return True
        
        return False
    
print(Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], 'ABCCED'))

print(Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], 'SEE'))

print(Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], 'ABCB'))
print(Solution().exist([["C","A","A"],["A","A","A"],["B","C","D"]], 'AAB'))

print(Solution().exist([["A", "A"]], 'AAA'))

print(
    Solution().exist(
        [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]], 'ABCESEEEFS')
)

print(
    Solution().exist(
        [["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"]], 'AAAAAAAAAAAAAAB')
)