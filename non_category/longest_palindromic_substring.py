# https://leetcode.com/problems/longest-palindromic-substring/solutions/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_start = 0
        longest_end = 1
        longest_substr = s[0]
        for i in range(0, len(s) - 1):
            right = i
            while right < len(s) and s[right] == s[i]:
                right += 1

            left = i - 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            left = left + 1
            if abs(right - left) > abs(longest_end - longest_start):
                longest_end, longest_start = right, left
                longest_substr = s[longest_start:longest_end]

        return longest_substr


test_case_1 = ('babad', ['bab', 'aba'])
test_case_2 = ('cbbd', ['bb'])
test_case_3 = ('abcba', ['abcba'])
test_case_4 = ('bb', ['bb'])
# for test_case in [test_case_1, test_case_2, test_case_3, test_case_4]:
for test_case in [test_case_4]:
    if Solution().longestPalindrome(test_case[0]) not in test_case[1]:
        print("Wrong")
