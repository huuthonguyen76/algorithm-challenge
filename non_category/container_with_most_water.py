# https://leetcode.com/problems/container-with-most-water/

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = -1
        i, j = 0, len(height) - 1
        while i < j:
            lowest_bar = min(height[i], height[j])

            cur_area = lowest_bar * (j - i)
            max_area = max(cur_area, max_area)

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return max_area


print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))
print(Solution().maxArea([1, 1]))
