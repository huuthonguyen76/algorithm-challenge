def solution(l_num, target):
    def __solution(l_num, target, cur_sum):
        for idx, num in enumerate(l_num):
            if cur_sum + num == target:
                return True

            if cur_sum + num < target:
                __solution(l_num[idx + 1:], target, cur_sum + num)

    __solution(l_num, target, 0)

l_num = [1, 6, 13, 5]
target = 30

solution(l_num, 11)
