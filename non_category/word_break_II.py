# https://leetcode.com/problems/word-break-ii/

from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        longest_length = 0
        d_vocab = {}
        l_final_result = []

        def solution(cur_s: str, l_cur_result: List[str]):
            if cur_s.strip() == '':
                if ' '.join(l_cur_result).strip() in l_final_result:
                    return True

                l_final_result.append(' '.join(l_cur_result).strip())
                return True

            for i in range(longest_length):
                if cur_s[:i + 1] in d_vocab:
                    solution(cur_s=cur_s[i + 1:], l_cur_result=l_cur_result + [cur_s[:i + 1]])
            
            return False

        d_vocab = {}
        for word in wordDict:
            longest_length = max(len(word), longest_length)
            d_vocab[word] = True
        
        solution(s, [])
        
        return l_final_result
        

test_case_1 = (('catsanddog', ["cat","cats","and","sand","dog"]), 2)
for test_case in [test_case_1]:
    print(test_case)
    if Solution().wordBreak(test_case[0][0], test_case[0][1]) != test_case[1]:
        print("Wrong")
