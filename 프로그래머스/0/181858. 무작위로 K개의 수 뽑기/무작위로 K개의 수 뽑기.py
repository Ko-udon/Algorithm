def solution(arr, k):
    answer = []
    for s in arr:
        if len(answer) == k:
            break
        if s not in answer:
            answer.append(s)
    return answer + [-1] * (k - len(answer))
