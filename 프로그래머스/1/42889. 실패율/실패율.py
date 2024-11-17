from collections import Counter
def solution(N, stages):
    total_people = len(stages)
    count_people = Counter(stages)

    answer = {} # 스테이지:실패율

    for i in range(1, N+1):
        answer[i] = 0

    for i in answer:
        if count_people[i] != 0 and total_people != 0:
            answer[i] = count_people[i]/total_people
        total_people -= count_people[i]

    return sorted(answer, key=lambda x:answer[x], reverse=True)