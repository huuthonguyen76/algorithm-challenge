# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, txt: str) -> int:
        i, j = 0, 0
        d_tracking = {}

        longest_len = 0
        cur_len = 0
        
        txt_len = len(txt)
        while True:
            while j < txt_len and txt[j] not in d_tracking:
                d_tracking[txt[j]] = j
                j += 1

            cur_len = j - i
            longest_len = max(cur_len, longest_len)

            if i >= txt_len or j >= txt_len:
                break

            i, j = d_tracking[txt[j]] + 1, d_tracking[txt[j]] + 1
            d_tracking = {}

        return longest_len


test_case_1 = ('abcabcbb', 3)
test_case_2 = ('bbbbb', 1)
test_case_3 = ('pwwkew', 3)

for test_case in [test_case_1, test_case_2, test_case_3]:
    if Solution().lengthOfLongestSubstring(test_case[0]) != test_case[1]:
        print("Wrong")
