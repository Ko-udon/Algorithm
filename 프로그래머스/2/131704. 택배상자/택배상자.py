def solution(order):
    answer = 0
    stack = []
    for i, o in enumerate(order):
        stack.append(i+1) # 택배상자 1, 2 순으로 넣기
        while stack and stack[-1] == order[answer]: # 스택이 비어있지 않고 제일 마지막 원소가 주문과 같으면
            stack.pop()
            answer +=1
    return answer