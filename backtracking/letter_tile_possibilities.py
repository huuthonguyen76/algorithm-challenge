# https://leetcode.com/problems/letter-tile-possibilities/description/?envType=problem-list-v2&envId=backtracking

from typing import List

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        self.result = 0
        l_tile_record = [0] * 26
        for tile in tiles:
            l_tile_record[ord(tile) - 65] += 1
        
        def recursive(l_tile_record: List[int]):
            self.result += 1

            for idx in range(len(l_tile_record)):
                if l_tile_record[idx] <= 0:
                    continue

                l_tile_record[idx] -= 1
                recursive(l_tile_record[:])
                l_tile_record[idx] += 1

        recursive(l_tile_record)
        
        return self.result - 1
            

print(Solution().numTilePossibilities("AAABBC"))
