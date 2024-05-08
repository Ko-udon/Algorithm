def solution(s):
    stack = list(s)
    # 맨 앞이나 뒤가 성립이 안되는 괄호인 경우
    if stack[-1] == "(" or stack[0] == ")":
        return False

    opened, closed = 0, 0

    while stack:
        if opened > closed:
            return False
        if stack[-1] == '(':
            opened += 1
            stack.pop()
        elif stack[-1]== ')':
            closed += 1
            stack.pop()
    return True if opened == closed else False