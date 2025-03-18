# https://leetcode.com/problems/beautiful-arrangement/?envType=problem-list-v2&envId=backtracking

from typing import List

class Solution:
    def countArrangement(self, n: int) -> int:
        self.result = 0

        l_num = [i + 1 for i in range(n)]

        def recursive(l_arr: List[int], l_cur_num: List[int], n: int):
            if len(l_cur_num) == 0:
                self.result += 1
                return 1

            for i in range(len(l_cur_num)):
                l_new_arr = l_arr + [l_cur_num[i]]
                if len(l_arr) >= 1:
                    if not(l_new_arr[-1] % (len(l_arr) + 1) == 0 or (len(l_arr) + 1) % l_new_arr[-1] == 0):
                        continue

                recursive(l_arr=l_new_arr, l_cur_num=l_cur_num[0:i] + l_cur_num[i + 1:], n=n)                
        
        recursive([], l_num, n)
        return self.result


Solution().countArrangement(2)