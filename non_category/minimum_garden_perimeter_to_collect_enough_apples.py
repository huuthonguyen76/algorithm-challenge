# https://leetcode.com/problems/minimum-garden-perimeter-to-collect-enough-apples/

class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        def get_perimeter(n):
            return n * 2 * 4

        def get_n_apple_layer_1(n):
            return n * 12
        
        # https://math.stackexchange.com/questions/2713656/how-to-calculate-sum-of-the-integers-from-m-to-n
        def get_n_apple_layer_2(n):
            lower_bound = n + 1
            upper_bound = n * 2 - 1

            return 8 * ((lower_bound + upper_bound) //2) * (upper_bound - lower_bound + 1)

        i = 1
        while neededApples >= 1:
            neededApples -= get_n_apple_layer_1(i) + get_n_apple_layer_2(i)
            i += 1

        return get_perimeter(i - 1)

test_case_1 = (1, 8)
test_case_2 = (13, 16)
test_case_3 = (1000000000, 5040)
# for test_case in [test_case_1, test_case_2, test_case_3]:
for test_case in [test_case_3]:
    print(Solution().minimumPerimeter(test_case[0]))
    print(Solution().minimumPerimeter(test_case[0]) == test_case[1])
