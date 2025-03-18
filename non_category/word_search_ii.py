# Link: https://leetcode.com/problems/word-search-ii/

from typing import List


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        s_result = set()
        l_first_chr = list(set([word[0] for word in words]))

        def add_border(board: List[List[str]]) -> List[List[str]]:
            new_board = []
            for _ in range(len(board) + 2):
                new_board.append(['.'] * (len(board[0]) + 2))

            for i in range(len(new_board)):
                for j in range(len(new_board[0])):
                    if i > 0 and i < len(new_board) - 1 and j > 0 and j < len(new_board[0]) - 1:
                        new_board[i][j] = board[i - 1][j - 1]
            
            return new_board
        
        def solution(board: List[List[str]], cur_track: str, cur_i: int, cur_j: int) -> None:
            if len(words) == 0:
                return

            if cur_track in words:
                s_result.add(cur_track)
                words.remove(cur_track)

            for next_jump in [(cur_i + 1, cur_j), (cur_i, cur_j + 1), (cur_i - 1, cur_j), (cur_i, cur_j - 1)]:
                if board[next_jump[0]][next_jump[1]] != '.':
                    before_chr = board[next_jump[0]][next_jump[1]]

                    board[next_jump[0]][next_jump[1]] = '.'
                    solution(board, cur_track=cur_track + before_chr, cur_i=next_jump[0], cur_j=next_jump[1])
                    board[next_jump[0]][next_jump[1]] = before_chr

        for i in range(len(board)):
            for j in range(len(board[0])):
                if len(words) == 0:
                    return list(s_result)

                l_first_chr = list(set([word[0] for word in words]))

                new_board = add_border(board)
                before_chr = new_board[i + 1][ j + 1]
                
                if before_chr not in l_first_chr:
                    continue

                new_board[i + 1][ j + 1] = '.'
                solution(new_board, before_chr, i + 1,  j + 1)

        print(len(s_result))
        return list(s_result)

test_case_1 = (([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], ["oath","pea","eat","rain"]), ["eat","oath"])
for test_case in [test_case_1]:
    if Solution().findWords(test_case_1[0][0], test_case_1[0][1]) != len(test_case_1[1]):
        print("Wrong")
