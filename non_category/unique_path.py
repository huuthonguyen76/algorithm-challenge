# Reference: https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        l_dp = [[0] * n for _ in range(m)]

        for idx in range(len(l_dp[0])):
            l_dp[0][idx] = 1

        for idx in range(len(l_dp)):
            l_dp[idx][0] = 1

        for i in range(len(l_dp)):
            if i == 0:
                continue

            for j in range(len(l_dp[0])):
                if j == 0:
                    continue

                l_dp[i][j] = l_dp[i - 1][j] + l_dp[i][j - 1]
        
        return l_dp[-1][-1]


test_case_1 = ((3, 2), 3)

for test_case in [test_case_1]:
    if Solution().uniquePaths(*test_case[0]) == test_case[1]:
        print("Pass")
