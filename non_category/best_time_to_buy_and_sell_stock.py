# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n_cur_max_profit = 0
        n_cur_min = 99999
        
        for price in prices:
            if price - n_cur_min > n_cur_max_profit:
                n_cur_max_profit = price - n_cur_min
            
            if price < n_cur_min:
                n_cur_min = price
        
        return n_cur_max_profit

test_case_1 = ([7, 1, 5, 3, 6, 4], 5)
for test_case in [test_case_1]:
    if Solution().maxProfit(test_case[0]) != test_case[1]:
        print("Wrong")



