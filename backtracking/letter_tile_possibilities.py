# https://leetcode.com/problems/letter-tile-possibilities/description/?envType=problem-list-v2&envId=backtracking

from typing import List

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        self.result = set()
        def recursive(s: str, l_cur_idx: List[int], l_cur_result: List[str]):
            self.result.add(''.join(l_cur_result))

            for idx in range(len(s)):
                if idx in l_cur_idx:
                    continue

                l_cur_idx.append(idx)
                l_cur_result.append(s[idx])
                recursive(s, l_cur_idx, l_cur_result)
                l_cur_idx.pop()
                l_cur_result.pop()

        recursive(tiles, [], [])
        self.result.remove('')
        return len(self.result) 
            

print(Solution().numTilePossibilities("AAB"))
