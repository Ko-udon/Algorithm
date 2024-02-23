from itertools import permutations

def solution(k, dungeons):
    answer = 0
    # permutations으로 모든 경우의 수 비교하기
    for p in permutations(range(len(dungeons))):
        # print(order)
        cur = k
        local_ans = 0
        for i in p:
            require, consum = dungeons[i]
            if cur >= require:
                cur -= consum
                local_ans += 1
        answer = max(answer, local_ans)


    return answer