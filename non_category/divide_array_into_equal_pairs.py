# https://leetcode.com/problems/divide-array-into-equal-pairs/

from typing import List
from collections import Counter

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        c_count = Counter()
        
        for num in nums:
            c_count[num] += 1
        
        for num, count in c_count.most_common():
            if count % 2 != 0:
                return False

        return True

test_case_1 = ([3,2,3,2,2,2], True)
test_case_2 = ([1,2,3,4], False)

for test_case in [test_case_1, test_case_2]:
    if Solution().divideArray((test_case[0])) != test_case[1]:
        print('Wrong')
