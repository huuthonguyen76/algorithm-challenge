from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort the intervals by the first element
        intervals.sort(key=lambda x: x[0])
        
        l_result = []
        
        l_cur_interval = intervals[0]
        for interval in intervals[1:]:
            if l_cur_interval[1] >= interval[0]:
                if l_cur_interval[1] <= interval[1]:
                    l_cur_interval = [l_cur_interval[0], interval[1]]
                else:
                    l_cur_interval = [l_cur_interval[0], l_cur_interval[1]]
            else:
                l_result.append(l_cur_interval[:])
                l_cur_interval = interval

        l_result.append(l_cur_interval[:])
        return l_result


intervals = [[1,3],[2,6],[8,10],[15,18]]
intervals = [[1,4],[4,5]]
print(Solution().merge(intervals))