# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/?envType=study-plan-v2&envId=top-interview-150

from typing import List

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1

        result = 0
        cur_count = 0
        d_cur_tracking = {}

        cursor = -1
        while cursor < len(s) - 1:
            cursor += 1

            if s[cursor] in d_cur_tracking:
                result = max(cur_count, result)
                cur_count = 0
                cursor = d_cur_tracking[s[cursor]]
                d_cur_tracking = {}
            else:
                d_cur_tracking[s[cursor]] = cursor
                cur_count += 1

        result = max(cur_count, result)
        return result

s = 'au'
print(Solution().lengthOfLongestSubstring(s))
