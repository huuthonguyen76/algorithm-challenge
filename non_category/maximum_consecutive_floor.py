# Link: https://leetcode.com/problems/maximum-consecutive-floors-without-special-floors/

from typing import List


class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        special = sorted(special)

        max_middle_floor = 0
        if len(special) != 1:
            for idx, _ in enumerate(special):
                if idx == 0:
                    continue
                
                max_middle_floor = max(special[idx] - special[idx - 1] - 1, max_middle_floor)

        left_floor = 0
        if bottom != special[0]:
            left_floor = special[0] - bottom
        
        right_floor = 0
        if top != special[-1]:
            right_floor = top - special[-1]

        return max([max_middle_floor, left_floor, right_floor])


    def sorting(self, l_num: List[int]):
        def __merge(l_num_1: List[int], l_num_2: List[int]):
            i, j = 0, 0
            l_merge = []
            while i < len(l_num_1) and j < len(l_num_2):
                if l_num_1[i] < l_num_2[j]:
                    l_merge.append(l_num_1[i])
                    i += 1
                else:
                    l_merge.append(l_num_2[j])
                    j += 1
            
            if i < len(l_num_1):
                l_merge += l_num_1[i:]
            
            if j < len(l_num_2):
                l_merge += l_num_2[j:]
            
            return l_merge
            
        if len(l_num) == 1:
            return l_num

        middle = len(l_num) // 2
        left = self.sorting(l_num[:middle])
        right = self.sorting(l_num[middle:])
        
        return __merge(left, right)

## Test case 1
bottom = 6
top = 8
special = [7, 6, 8]

# ## Test case 2   
# bottom = 2
# top = 9
# special = [4, 6]

## Test case 3
bottom = 10
top = 30
special = [19,10,15]

print(Solution().maxConsecutive(bottom, top, special))

# print(Solution().sorting(special))

