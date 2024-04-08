from itertools import permutations as perm
from collections import deque
# https://2hs-rti.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-Lv2-%EC%88%98%EC%8B%9D-%EC%B5%9C%EB%8C%80%ED%99%94-%ED%8C%8C%EC%9D%B4%EC%8D%AC 참조..

def solution(expression):
    answer = 0
    for priority in list(perm(['+', '-', '*'], 3)):
        answer = max(answer, abs(make_result(priority, expression)))
    return answer


def make_result(priority, expression):
    # arr 만들기
    arr = deque()
    num = ''
    for k in expression:
        if k.isdigit():
            num += k
        else:
            arr.append(num)
            num = ''
            arr.append(k)
    arr.append(num)
    # 계산
    for op in priority:
        stack = []
        while len(arr) != 0:
            temp = arr.popleft()
            if temp == op:
                result = str(eval(stack.pop()+op+arr.popleft()))
                stack.append(result)
            else:
                stack.append(temp)
        arr = deque(stack)
    return int(arr.pop())
# 레벨 2 맞나?..