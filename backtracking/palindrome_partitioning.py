# https://leetcode.com/problems/palindrome-partitioning/?envType=problem-list-v2&envId=backtracking

from typing import List


class Solution:
    def is_paplindrome(self, s: str):
        l, r = 0, len(s) - 1

        while True:
            if l > r:
                break
            
            if s[l] != s[r]:
                return False

            l += 1
            r -= 1
        
        return True

    def partition(self, s: str) -> List[List[str]]:
        self.result = []
        self.cache_is_palindrome = set()

        def recursive(s: str, tracking: List[str]):
            if s == '':
                self.result.append(tracking[:])
                return

            for idx in range(1, len(s) + 1):
                cur_s = s[:idx]
                if not cur_s in self.cache_is_palindrome and not self.is_paplindrome(s[:idx]):
                    continue
                
                self.cache_is_palindrome.add(s[:idx])

                tracking.append(s[:idx])
                recursive(s[idx:], tracking[:])
                tracking.pop()

        recursive(s, [])
        return self.result

s = "baab"
print(Solution().partition(s))
