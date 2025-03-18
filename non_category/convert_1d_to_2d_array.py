# https://leetcode.com/problems/convert-1d-array-into-2d-array/

import numpy as np

from typing import List


class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        try:
            np_original = np.asarray(original)
            result = list(np_original.reshape(m, n))
        except:
            return []

        return result


print(Solution().construct2DArray([1,2,3,4], 2, 2))
