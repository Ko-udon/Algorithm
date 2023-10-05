def solution(sizes):
    # 가로, 세로 길이 중 길이가 큰 애들 중에서 가장 큰 값, 길이가 작은 애들 중에서 가장 큰 값
    return max(max(i) for i in sizes) * max(min(i) for i in sizes)