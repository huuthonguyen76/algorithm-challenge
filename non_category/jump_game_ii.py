# https://leetcode.com/problems/jump-game-ii/

from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        if nums[0] >= len(nums) - 1:
            return 1

        cursor = 0
        n_min_step = 0
        while True:
            if cursor >= len(nums) - 1:
                break

            n_min_step += 1
            next_jump = nums[cursor]

            max_jump = -1
            max_pos = -1
            for i in range(cursor, cursor + next_jump + 1, 1):
                if i == cursor:
                    continue
                
                estimated_jump = i + nums[i]
                if estimated_jump >= len(nums) -1:
                    n_min_step += 1
                    return n_min_step

                if estimated_jump > max_jump:
                    max_jump = estimated_jump
                    max_pos = i

            cursor = max_pos

        return n_min_step


test_case_1 = ([2,3,1,1,4], 2)
test_case_2 = ([2,3,0,1,4], 2)

test_case_3 = ([1,2], 1)
test_case_4 = ([0], 0)
test_case_5 = ([2, 1], 1)
test_case_6 = ([4,1,1,3,1,1,1], 2)
test_case_7 = ([1, 2, 3], 2)

test_case_8 = ([1, 3, 2], 2)
test_case_8 = ([3, 2, 1], 2)

for test_case in [ test_case_1, test_case_2, test_case_3, test_case_4, test_case_5, test_case_6, test_case_7]:
# for test_case in [test_case_8]:
    if Solution().jump(test_case[0]) != test_case[1]:
        print("Wrong", Solution().jump(test_case[0]), test_case)
