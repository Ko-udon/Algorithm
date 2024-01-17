def solution(num_list):
    return sum(num_list) if len(num_list) >= 11 else multiply(num_list)

def multiply(arr):
    n = 1
    for v in arr:
        n *= v
    return n