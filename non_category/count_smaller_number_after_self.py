# Link: https://leetcode.com/problems/count-of-smaller-numbers-after-self/

from typing import List


class Element:
    def __init__(self, pos: int, val: int, smaller_element: int) -> None:
        self.pos = pos
        self.val = val
        self.smaller_element = smaller_element
    
    def __str__(self) -> str:
        return str(self.val)


class Solution:
    def __init__(self) -> None:
        self.result = []

    def countSmaller(self, nums: List[int]) -> List[int]:
        self.result = [0] * len(nums)
        _ = self.sorting(nums, 0, len(nums))
        return self.result

    def merge(self, l_left: List[Element], l_right: List[Element]) -> List[Element]:
        l_merge = []
        i, j = 0, 0
        while i < len(l_left) and j < len(l_right):
            if l_left[i].val > l_right[j].val:
                l_left[i].smaller_element = l_left[i].smaller_element + len(l_right[j:])
                l_merge.append(l_left[i])
                self.result[l_left[i].pos] = l_left[i].smaller_element
                i += 1
            else:
                l_merge.append(l_right[j])
                j += 1
    
        if i < len(l_left):
            l_merge += l_left[i:]
        
        if j < len(l_right):
            l_merge += l_right[j:]

        return l_merge

    def sorting(self, nums: List[Element], i: int, j: int) -> List[Element]:
        if (j - i) == 1:
            return [Element(i, nums[i], 0)]

        middle = (i + j) // 2
        left = self.sorting(nums, i, middle)
        right = self.sorting(nums, middle, j)

        return self.merge(left, right)
    
    def print_list(self, l_element: List[Element]) -> str:
        print(' '.join([f'{element.val},{element.smaller_element}' for element in l_element]))

test_case_1 = ([5, 2, 6, 1], [2, 1, 1, 0])
test_case_1 = ([2,0,1], [2, 0, 0])

for test_case in [test_case_1]:
    test_case_input = test_case[0]
    test_case_output = test_case[1]
    
    if Solution().countSmaller(test_case_input) != test_case_output:
        print("Wrong")

