# https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/


class Solution:
    def splitString(self, s: str) -> bool:
        def solution(s: str, prev_val: int, i: int, length: int):
            while i + length < len(s):
                length += 1
                cur_val = int(s[i:i+length])
                if prev_val == -1:
                    is_valid = solution(s=s, prev_val=cur_val, i=i+length, length=0)
                    if is_valid:
                        return True

                if prev_val - cur_val == 1:
                    if i + length >= len(s):
                        return True

                    if s[i+length:].rstrip('0') == '' and cur_val == 1:
                        return True

                    if prev_val == 1 and s[i:].rstrip('0') == '':
                        return True

                    return solution(s=s, prev_val=cur_val, i=i+length, length=0)

            return False

        result = solution(s, -1, 0, 0)
        return result
            


test_case_1 = ("1234", False)
test_case_2 = ("050043", True)
# test_case_2 = ("7675", True)
test_case_3 = ("9080706", True)
test_case_4 = ("100", True)
test_case_4 = ("001", False)
test_case_5 = ("43420", False)
test_case_6 = ("1000", True)
# for test_case in [test_case_1, test_case_2, test_case_3]:
for test_case in [test_case_6]:
    if Solution().splitString(test_case[0]) != test_case[1]:
        print("Wrong")
