class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        l_new_array = []
        for i in range(numRows):
            l_new_array.append([])
                
        s_checked_pos = set()
        l_cursor = 0
        
        if numRows == 2:
            jump_level = 2
        else:
            jump_level = numRows + numRows - 2

        r_cursor = l_cursor + jump_level
        while l_cursor <= len(s):
            cur_lvl = 0
            
            new_l_cursor = l_cursor
            while new_l_cursor <= r_cursor:
                if new_l_cursor == r_cursor:
                    if new_l_cursor <= (len(s)) - 1 and new_l_cursor not in s_checked_pos:
                        l_new_array[cur_lvl].append(s[new_l_cursor])
                        s_checked_pos.add(new_l_cursor)
                    break
                else:
                    if new_l_cursor <= len(s) - 1 and new_l_cursor not in s_checked_pos:
                        l_new_array[cur_lvl].append(s[new_l_cursor])
                        s_checked_pos.add(new_l_cursor)
                    if r_cursor <= len(s) - 1 and r_cursor not in s_checked_pos:
                        l_new_array[cur_lvl].append(s[r_cursor])
                        s_checked_pos.add(r_cursor)

                    new_l_cursor += 1
                    r_cursor -= 1
                    cur_lvl += 1

            l_cursor += jump_level
            r_cursor = l_cursor + jump_level

        result = ''
        for ele in l_new_array:
            result += ''.join(ele)
        
        return result

s = 'PAYPALISHIRING'
numRows = 4

print(Solution().convert(s, numRows))
