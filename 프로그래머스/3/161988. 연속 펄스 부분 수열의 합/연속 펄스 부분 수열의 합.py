def solution(sequence):
    v = [0]
    for i, s in enumerate(sequence): 
        v.append(v[-1] + s * [1, -1][i%2]) # 제일 뒤 값 + 다음 값 * 1 또는 -1(원소 순서에 따라)
    return max(v) - min(v)