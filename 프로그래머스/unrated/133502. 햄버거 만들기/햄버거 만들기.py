def solution(ingredient):
    answer = 0
    buger = [1, 2, 3, 1]
    stack = []

    for i in ingredient:
        stack.append(i)
        if len(stack) >= 4 and stack[-4:] == buger:
            answer += 1
            for s in range(4):
                stack.pop()
    return answer