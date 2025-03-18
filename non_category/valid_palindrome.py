import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub(r'[^a-zA-Z0-9]', '', s)

        i, j = 0, len(s) - 1
        
        if s.strip() == 0:
            return True

        while True:
            if i >= j:
                return True

            if s[i] != s[j]:
                return False

            i += 1
            j -= 1

        return True

print(Solution().isPalindrome('0P'))
