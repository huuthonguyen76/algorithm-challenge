# https://leetcode.com/problems/reverse-words-in-a-string/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(list(filter(lambda x: x!= '', s.split(' ')))[::-1])
    

print(Solution().reverseWords("a good   example"))
