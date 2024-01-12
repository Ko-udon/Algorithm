def solution(my_string, is_prefix):
    arr = list(my_string[:i] for i in range(1, len(my_string)))
    return 1 if is_prefix in arr else 0