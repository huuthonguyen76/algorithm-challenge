# Link: https://leetcode.com/problems/reverse-words-in-a-string-iii/


class Solution:
    def reverseWords(self, s: str) -> str:
        result = ''
        for word in s.split(' '):
            result += word[::-1] + ' '

        return result.strip()


test_case_1 = ("Let's take LeetCode contest", "s'teL ekat edoCteeL tsetnoc")
test_case_2 = ("God Ding", "doG gniD")

for test_case in [test_case_1, test_case_2]:
    input_test_case, output_test_case = test_case
    if Solution().reverseWords(input_test_case) != output_test_case:
        print("Wrong: ", test_case)
        print('Expected: ', output_test_case)
        print('Current: ', Solution().reverseWords(input_test_case))
        print('-' * 5)
