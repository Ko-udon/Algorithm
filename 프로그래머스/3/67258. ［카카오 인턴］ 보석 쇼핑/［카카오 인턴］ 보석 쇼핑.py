from collections import Counter
def solution(gems):
    answer = []
    list_gems = list(set(gems))
    cnt_gems = Counter(gems) # gems종류별로 그 개수 저장
    left, right = 0, 0
    
    # 최소가 되는 right 구하기
    for r in range(len(gems)-1, -1, -1):
        if cnt_gems[gems[r]] == 1:
            right = r
            break
        cnt_gems[gems[r]] -= 1

    
    for r in range(right, len(gems)):
        while left < r:
            if left < len(gems) and cnt_gems[gems[left]] == 1:
                break
            cnt_gems[gems[left]] -= 1
            left += 1
        answer.append([left+1, r+1])
        if r+1 < len(gems):
            cnt_gems[gems[r+1]] += 1
    return sorted(answer, key=lambda x:(x[1]-x[0], x[0]))[0]
