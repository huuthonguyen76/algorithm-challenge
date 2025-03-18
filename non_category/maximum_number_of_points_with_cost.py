from typing import List

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        for i, _ in enumerate(points):
            if i == 0:
                continue
            
            if len(points[i]) == 1:
                points[i][0] += points[i - 1][0]
                continue

            l, r = [0] * len(points[0]), [0] * len(points[0])
            l[0]  = points[i - 1][0]
            r[-1] = points[i - 1][-1]
            for j in range(0, len(l), 1):
                if j == 0:
                    continue
                
                l[j] = max(points[i - 1][j], l[j - 1] - 1)
            
            for j in range(len(l) - 1, -1, -1):
                if j == len(l) - 1:
                    continue

                r[j] = max(points[i - 1][j], r[j + 1] - 1)

            for j in range(0, len(points[0]), 1):
                points[i][j] = max(points[i][j] + l[j], points[i][j] + r[j])
        
        return max(points[-1])


points = [[0,3,0,4,2],[5,4,2,4,1],[5,0,0,5,1],[2,0,1,0,3]]
print(Solution().maxPoints(points))
