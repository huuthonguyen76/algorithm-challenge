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
        def recursive():
            pass
        
        pass

s = "baab"
print(Solution().is_paplindrome(s))
