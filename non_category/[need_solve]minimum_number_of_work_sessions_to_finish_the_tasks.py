# https://leetcode.com/problems/minimum-number-of-work-sessions-to-finish-the-tasks/description/?envType=problem-list-v2&envId=dynamic-programming

from typing import List

class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        d_tracking = {
            'count': 0
        }

        def recursive(tasks: List[int], target: int, rest: int, d_tracking: dict):
            if rest < 0:
                return 0

            if rest == 0:
                d_tracking['count'] += 1
                return 1

            for i in range(len(tasks)):
                if tasks[i] == -1:
                    continue

                cur_hour = tasks[i]
                tasks[i] = -1
                result = recursive(tasks, target, rest - cur_hour, d_tracking)
                if result == 0:
                    tasks[i] = cur_hour
                else:
                    if rest < target:
                        return 1
                    else:
                        continue
            
            return 0

        tasks = sorted(tasks)

        recursive(tasks, sessionTime, sessionTime, d_tracking)
        print(tasks)
        print(d_tracking)
        n_cur_sum = 0
        n_more_count = 0
        for ele in tasks:
            if ele == -1:
                continue
            
            n_cur_sum += ele 
            if n_cur_sum > sessionTime:
                n_more_count += 1
                n_cur_sum = ele
        
        if n_cur_sum > 0:
            n_more_count += 1

        return d_tracking['count'] + n_more_count


tasks = [1, 2]
sessionTime = 5

tasks = [3,1,3,1,1]
sessionTime = 8

tasks = [2,3,3,4,4,4,5,6,7,10]
sessionTime = 12
result = Solution().minSessions(tasks, sessionTime)
print(result)
    