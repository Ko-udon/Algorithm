def solution(str_list):
    if "l" not in str_list and "r" not in str_list:
        return []
    for s in str_list:
        if s == "r":
            n = str_list.index(s)
            return str_list[n+1:]
        elif s == "l":
            n = str_list.index(s)
            return str_list[:n]