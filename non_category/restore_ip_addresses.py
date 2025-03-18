# https://leetcode.com/problems/restore-ip-addresses/

from typing import List

class Solution:
    def is_valid(self, l_txt: List[str]) -> bool:
        for ele in l_txt:
            ele = str(ele)
            if ele == '':
                return False
                
            if ele[0] == '0' and len(ele) > 1:
                return False

            if int(ele) > 255 or int(ele) < 0:
                return False

        return True

    def restoreIpAddresses(self, s: str) -> List[str]:
        l_result = []
        def solution(cur_string: str, l_cur_solution: List[int]):
            if len(l_cur_solution) == 4 and self.is_valid(l_cur_solution):
                l_result.append('.'.join(l_cur_solution[:]).rstrip('.'))
                return

            length = 1
            while len(l_cur_solution) < 4:
                cur_next_string = cur_string[:length]
                if cur_next_string == '':
                    break
                
                if len(l_cur_solution) == 3:
                    solution('', l_cur_solution + [cur_string])
                    break

                # Meant it reach the limit
                if len(cur_next_string) != length:
                    return

                if cur_next_string[0] == '0' and len(cur_next_string) > 1:
                    return
                
                if int(cur_next_string) > 255:
                    return

                solution(cur_string[length:], l_cur_solution + [cur_next_string])
                length += 1
                
            return
        
        solution(s, [])
        print(l_result)
        return l_result
    
test_case_1 = ('25525511135', 2)
test_case_2 = ('0000', 1)
test_case_3 = ('101023', 5)
test_case_4 = ('1111', 1)

for test_case in [test_case_1, test_case_2, test_case_3, test_case_4]:
    print(len(Solution().restoreIpAddresses(test_case[0])) == test_case[1])
