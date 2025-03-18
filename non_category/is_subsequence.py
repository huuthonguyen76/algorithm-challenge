# https://leetcode.com/problems/is-subsequence/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        t_cursor = 0
        s_cursor = 0
        
        while s_cursor < len(s) and t_cursor < len(t):
            if s[s_cursor] == t[t_cursor]:
                s_cursor += 1

            t_cursor += 1
        
        return s_cursor >= len(s)

s = "axc"
t = "ahbgdc"

print(Solution().isSubsequence(s, t))