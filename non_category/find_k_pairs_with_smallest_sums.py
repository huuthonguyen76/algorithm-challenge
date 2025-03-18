# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/description/?envType=study-plan-v2&envId=top-interview-150

from typing import List

class Solution:
    def insert_heap(self, nums, val):
        nums.append(val)
        cur_pos = len(nums) - 1
        while cur_pos > 0:
            parent_pos = (cur_pos - 1) // 2
            if nums[cur_pos] <= nums[parent_pos]:
                nums[cur_pos], nums[parent_pos] = nums[parent_pos], nums[cur_pos]

            cur_pos = parent_pos
        
        return nums
    
    def remove_element(self, l_heap):
        l_heap[0], l_heap[-1] = l_heap[-1], l_heap[0]
        l_heap = l_heap[:-1]
        cur_pos = 0
        while cur_pos < len(l_heap) - 1:
            left, right = cur_pos * 2 + 1, cur_pos * 2 + 2
            
            if right <= len(l_heap) - 1:
                if l_heap[left] < l_heap[right]:
                    next_pos = left
                else:
                    next_pos = right
            elif left <= len(l_heap) - 1:
                next_pos = left
            else:
                break

            if l_heap[cur_pos] > l_heap[next_pos]:
                l_heap[cur_pos], l_heap[next_pos] = l_heap[next_pos], l_heap[cur_pos]
            else:
                break
            
            cur_pos = next_pos
        
        return l_heap
        
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        min_num_1 = min(nums1)
        min_num_2 = min(nums2)
        
        if min_num_1 > min_num_2:
            nums1, nums2 = nums2, nums1
            min_num_1, min_num_2 = min_num_2, min_num_1
        
        l_heap = []
        for num in nums2:
            l_heap = Solution().insert_heap(l_heap, num)

        l_pair = []
        for _ in range(k):
            l_pair.append((min_num_1, l_heap[0]))
            l_heap = Solution().remove_element(l_heap)
        
        return l_pair


# l_heap = []
# nums_test_heap = [5, 10, 1, 3, 6, 13, 14, 8]
# for num in nums_test_heap:
#     l_heap = Solution().insert_heap(l_heap, num)

# l_heap = Solution().remove_element(l_heap)
# print(l_heap)

# l_heap = Solution().remove_element(l_heap)
# print(l_heap)

nums1 = [1, 7, 11]
nums2 = [2, 4, 6]
k = 3

Solution().kSmallestPairs(nums1, nums2, k)