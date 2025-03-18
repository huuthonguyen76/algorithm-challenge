# Link: https://leetcode.com/problems/merge-sorted-array/?envType=study-plan-v2&envId=top-interview-150

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l_result = []
        left_cursor  = 0
        right_cursor = 0
        
        print(nums1, m, nums2, n)
        while True:
            if left_cursor >= m and right_cursor >= n:
                break

            if left_cursor < m:
                left_num = nums1[left_cursor]
            else:
                left_num = float('inf')

            if right_cursor < n:
                right_num = nums2[right_cursor]
            else:
                right_num = float('inf')

            if left_num < right_num:
                l_result.append(nums1[left_cursor])
                left_cursor += 1
                continue
            else:
                l_result.append(nums2[right_cursor])
                right_cursor += 1
                continue

        return l_result

test_case_1 = (([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3), [1, 2, 2, 3, 5, 6])
for test_case in [test_case_1]:
    print(Solution().merge(test_case[0][0], test_case[0][1], test_case[0][2], test_case[0][3]))
    # print(Solution().merge(test_case[0][0], test_case[0][1], test_case[0][2], test_case[0][3]) == test_case[1])
