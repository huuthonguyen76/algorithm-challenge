# https://leetcode.com/problems/minimum-distance-to-the-target-element/

from typing import List


class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        min_distance = 999999
        for i in range(len(nums)):
            if nums[i] == target:
                min_distance = min(abs(i - start), min_distance)
        return min_distance


test_case_1 = (([1,2,3,4,5], 5, 3), 1)
test_case_2 = (([1], 1, 0), 0)
test_case_3 = (([1,1,1,1,1,1,1,1,1,1], 1, 0), 0)

for test_case in [test_case_1]:
    if Solution().getMinDistance(test_case[0][0], test_case[0][1], test_case[0][2]) != test_case[1]:
        print("Wrong")
