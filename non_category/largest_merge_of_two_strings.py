# Link: https://leetcode.com/problems/largest-merge-of-two-strings/

class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        l_merge = []
        while i < len(word1) and j < len(word2):
            if word1[i:] > word2[j:]:
                l_merge.append(word1[i])
                i += 1
            else:
                l_merge.append(word2[j])
                j += 1

            # print(word1[i:])
            # print(word2[j:])
            # print(''.join(l_merge))
            # print('-' * 5)

        if i < len(word1):
            l_merge += word1[i:]

        if j < len(word2):
            l_merge += word2[j:]

        # print(''.join(l_merge))
        return ''.join(l_merge)
        
test_case_1 = ('cabaa', 'bcaaa')
output_1 = 'cbcabaaaaa'

print(Solution().largestMerge(test_case_1[0], test_case_1[1]) == output_1)
