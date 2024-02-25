from collections import deque

def solution(priorities, location):
    answer = 0
    # deque 생성
    dq = deque([(v,i) for i,v in enumerate(priorities)])

    while len(dq):
        item = dq.popleft()
        # pop한 아이템이 우선순위가 낮은 경우 다시 큐에 추가
        if dq and max(dq)[0] > item[0]:
            dq.append(item)
        else:
            answer += 1
            if item[1] == location:
                break
    return answer