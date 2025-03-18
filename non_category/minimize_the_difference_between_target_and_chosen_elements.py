# https://leetcode.com/problems/minimize-the-difference-between-target-and-chosen-elements/description/?envType=problem-list-v2&envId=dynamic-programming

from typing import List


class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        s_next_row = mat.pop()

        for row in mat:
            s_next_row = {
                x + i
                for x in set(row)
                for i in s_next_row
            }

        n_min = 999999
        for ele in s_next_row:
            if abs(target - ele) < n_min:
                n_min = abs(target - ele)
        print(n_min)
        return n_min
        
mat = [[1,2,3],[4,5,6],[7,8,9]]
target = 13
Solution().minimizeTheDifference(mat, target)