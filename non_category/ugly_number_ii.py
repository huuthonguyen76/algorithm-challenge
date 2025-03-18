# https://leetcode.com/problems/ugly-number-ii/description/

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n <= 5:
            return n

        d_track = {
            1: True,
            2: True,
            3: True,
            4: True,
            5: True
        }
        l_num = [1, 2, 3, 4, 5]
        cursor_2 = 0
        cursor_3 = 0
        cursor_5 = 0
        while True:
            next_ele = min(l_num[cursor_2] * 2, l_num[cursor_3] * 3, l_num[cursor_5] * 5)
            if next_ele == l_num[cursor_2] * 2:
                cursor_2 += 1
            
            if next_ele == l_num[cursor_3] * 3:
                cursor_3 += 1
            
            if next_ele == l_num[cursor_5] * 5:
                cursor_5 += 1

            if next_ele not in d_track:
                l_num.append(next_ele)
                d_track[next_ele] = True

            if len(l_num) >= n:
                break

        return l_num[n - 1]


test_case_1 = (11, 15)
for test_case in [test_case_1]:
    if Solution().nthUglyNumber(test_case[0]) != test_case_1[1]:
        print('Fail: ', test_case_1)
