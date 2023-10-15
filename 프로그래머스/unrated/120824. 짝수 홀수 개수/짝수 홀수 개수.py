def solution(num_list):
    odds = len(list(filter(lambda x:x%2 == 0, num_list)))
    print(odds)
    return [odds, len(num_list) - odds]