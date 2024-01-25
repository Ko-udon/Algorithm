def solution(nums):
    case1 = len(nums) / 2
    case2 = len(set(nums))
    return min(case1, case2)