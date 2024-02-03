def solution(s):
    stack = list(s)
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

    if opened == closed :
        return True
    else:
        return False
        