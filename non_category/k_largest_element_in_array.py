# https://leetcode.com/problems/kth-largest-element-in-an-array/

from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def heapify(nums: List[int], i: int) -> int:
            if i >= len(nums):
                return 9999999

            left_idx = i * 2
            right_idx = 1 + (i * 2)

            heapify(nums, left_idx)
            heapify(nums, right_idx)

            if left_idx <= len(nums) - 1:
                if nums[i] > nums[left_idx]:
                    nums[i], nums[left_idx] = nums[left_idx], nums[i]
            
            if right_idx <= len(nums) - 1:
                if nums[i] > nums[right_idx]:
                    nums[i], nums[right_idx] = nums[right_idx], nums[i]

            return nums[i]

        heap = [9999999] + nums[:k]
        for i in range(len(heap)):
            if i == 0:
                continue

            heapify(heap, i)

        for ele in nums[k:]:
            if ele > heap[1]:
                heap[1] = ele
                heapify(heap, 1)

        return heap[1]

test_case_1 = (([3,2,1,5,6,4], 2), 5)
test_case_2 = (([3,2,3,1,2,4,5,5,6], 4), 4)

for test_case in [test_case_1, test_case_2]:
    if Solution().findKthLargest(test_case[0][0], test_case[0][1]) != test_case[1]:
        print("Wrong")

# print(Solution().findKthLargest([3,2,1,5,6,4], 5))