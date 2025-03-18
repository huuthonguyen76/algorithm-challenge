# https://leetcode.com/problems/median-of-two-sorted-arrays/


from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i, j = 0, 0
        middle_1, middle_2 = 0, 0
        
        if len(nums1) == 0:
            if len(nums2) % 2 == 0:
                middle = len(nums2) // 2
                return (nums2[middle] + nums2[middle - 1]) / 2
            else:
                middle = len(nums2) // 2
                return nums2[middle]
        
        if len(nums2) == 0:
            if len(nums1) % 2 == 0:
                middle = len(nums1) // 2
                return (nums1[middle] + nums1[middle - 1]) / 2
            else:
                middle = len(nums1) // 2
                return nums1[middle]

        is_odd = (len(nums1) + len(nums2)) % 2 != 0
        if is_odd:
            middle_1 = (len(nums1) + len(nums2)) // 2
        else:
            middle_1 = (len(nums1) + len(nums2)) // 2 - 1
            middle_2 = (len(nums1) + len(nums2)) // 2 

        l_tracking = []
        while i < len(nums1) and j < len(nums2):
            if len(l_tracking) != 0:
                if is_odd:
                    if len(l_tracking) - 1 >= middle_1:
                        return l_tracking[middle_1]
                else:
                    if len(l_tracking) - 1 >= middle_2:
                        return (l_tracking[middle_1] + l_tracking[middle_2]) / 2

            if nums1[i] <= nums2[j]:
                l_tracking.append(nums1[i])
                i += 1
            else:
                l_tracking.append(nums2[j])
                j += 1
            
        if i < len(nums1):
            l_tracking = l_tracking + nums1[i:]
        
        if j < len(nums2):
            l_tracking = l_tracking + nums2[j:]
        
        if is_odd:
            if len(l_tracking) - 1 >= middle_1:
                return l_tracking[middle_1]
        else:
            if len(l_tracking) - 1 >= middle_2:
                return (l_tracking[middle_1] + l_tracking[middle_2]) / 2

test_case_1 = (([1, 3], [2]), 2)
test_case_2 = (([1, 2], [3, 4]), 2.5)
test_case_3 = (([1, 2, 3], []), 2)
test_case_4 = (([], [1, 2, 3 , 4]), 2.5)

for test_case in [test_case_1, test_case_2, test_case_3, test_case_4]:
    if Solution().findMedianSortedArrays(test_case[0][0], test_case[0][1]) != test_case[1]:
        print("Wrong")
