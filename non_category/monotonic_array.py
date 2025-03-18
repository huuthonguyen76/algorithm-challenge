# Link: https://leetcode.com/problems/monotonic-array/

from typing import List

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        def is_valid(num_1:int, num_2: int, is_up: bool):
            if is_up:
                return num_1 <= num_2
            else:
                return num_1 >= num_2

        is_up = None
        for idx, _ in enumerate(nums):
            if idx == 0:
                continue

            if is_up is None:
                if nums[idx] - nums[idx - 1] == 0:
                    continue
                else:
                    if nums[idx] - nums[idx - 1] > 0:
                        is_up = True
                    else:
                        is_up = False
            else:
                if not is_valid(nums[idx - 1], nums[idx], is_up):
                    return False
        
        return True

l_test_case_1 = [1, 2, 2, 3]
l_test_case_2 = [6, 5, 4, 4]
l_test_case_3 = [1, 3, 2]
l_test_case_4 = [1, 1, 0]

for test_case in [l_test_case_1, l_test_case_2, l_test_case_3, l_test_case_4]:
    print(Solution().isMonotonic(test_case))
