from collections import Counter
def solution(weights):
    answer = 0
    counter = Counter(weights)

    for i in counter:
        answer += counter[i] * (counter[i] - 1) // 2 # 같은 수가 있는 경우
        answer += counter[i] * counter[i * 3 / 2] # 1.5배, 2m, 3m, 4m 경우
        answer += counter[i] * counter[i * 2] # 2배, 2m, 4m 경우
        answer += counter[i] * counter[i * 4 / 3] # 
    return answer