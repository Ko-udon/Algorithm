def solution(food):
    front = ''
    for s in range(1, len(food)):
        n = food[s] // 2
        front += str(s) * n
    return front + '0' + front[::-1]