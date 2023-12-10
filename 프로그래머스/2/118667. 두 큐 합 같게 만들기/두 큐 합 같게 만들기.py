from collections import deque

def solution(queue1, queue2):
    
    if (sum(queue1) + sum(queue2)) % 2 != 0:
        return -1
    answer = 0
    dq_1 = deque(queue1)
    dq_2 = deque(queue2)
    limit = len(queue1) * 4 # 반복 탈출 조건으로 교환 횟수 제한
    # 큐 1과2가 서로의 모든 원소를 바꾸더라도 하나의 큐 길이의 두배 만큼의 길이가 필요하고 
    # 이는 두 큐가 값이 같아지는 조건이 아니라 계속해서 원소를 교환해야되는데
    # 최대로 바꿔서 서로 원래대로의 큐로 돌아오더라도 또 큐 길이의 두배 만큼 횟수가 필요하므로 길이의 * 4
    
    total_1 = sum(dq_1)
    total_2 = sum(dq_2)
    
    while True:
        if total_1 > total_2:
            tmp = dq_1.popleft()
            dq_2.append(tmp)
            total_1 -= tmp
            total_2 += tmp
            answer += 1
            
        elif total_1 < total_2:
            tmp = dq_2.popleft()
            dq_1.append(tmp)
            total_1 += tmp
            total_2 -= tmp
            answer += 1
            
        else: # 둘이 같으면 합격!
            break
            
        if answer >= limit:
            answer = -1
            break
    
    return answer