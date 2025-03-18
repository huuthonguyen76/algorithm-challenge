from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        l_row = []
        for n in range(1, numRows + 1, 1):
            l_row.append([1] * (n))
        
        if numRows <= 2:
            return l_row

        for i in range(2, numRows, 1):
            for j in range(len(l_row[i])):
                if j == 0 or j == len(l_row[i]) - 1:
                    continue

                l_row[i][j] = l_row[i - 1][j - 1] + l_row[i - 1][j]
        
        return l_row
            

n_row = 5
print(Solution().generate(n_row))
        