def solution(numbers):
    numbers_str = list(map(str, numbers))
    
    # 문자열 비교를 통해 정렬, 1000까지라서 x*3
    numbers_str.sort(key=lambda x: x*3, reverse=True)
    
    answer = ''.join(numbers_str)
    return str(int(answer))