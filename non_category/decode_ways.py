# https://leetcode.com/problems/decode-ways/


class Solution:
    def numDecodings(self, s: str) -> int:
        l_n_way = [0] * len(s)

        if '00' in s:
            return 0

        if s[0] == '0':
            return 0

        if len(s) == 1:
            return 1

        if len(s) == 2:
            if int(s) <= 10:
                return 1

            if 11 <= int(s) and int(s) <= 26 and int(s) != 20:
                return 2

            if int(s) > 26 and int(s[1]) == 0:
                return 0

            return 1

        # Set initial step
        if s[0] != '0':
            l_n_way[0] = 1

        if 1 <= int(s[0] + s[1]) <= 10:
            l_n_way[1] = 1
        elif 11 <= int(s[0] + s[1]) <= 26 and int(s[0] + s[1]) != 20:
            l_n_way[1] = 2
        else:
            l_n_way[1] = 1
        
        if int(s[0] + s[1]) >= 26 and int(s[1]) == 0:
            l_n_way[1] = 0

        for idx, _ in enumerate(s):
            if idx <= 1:
                continue

            if 1 <= int(s[idx]) and int(s[idx]) <= 9:
                l_n_way[idx] += l_n_way[idx - 1]

            if 10 <= int(s[idx - 1] + s[idx]) and int(s[idx - 1] + s[idx]) <= 26:
                l_n_way[idx] += l_n_way[idx - 2]

        return l_n_way[-1]

print(Solution().numDecodings('207'))
