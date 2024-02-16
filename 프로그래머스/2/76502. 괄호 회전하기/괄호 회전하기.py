def solution(s):
    answer = 0
    arr = list(s)
    for i in range(len(s)):
        bracket = ''.join(arr)
        arr = rotate(arr)
        if check(bracket):
            answer += 1
    return answer

def rotate(arr):
    return arr[1:] + arr[:1]

def check(s):
    stack = []
    for i in s:
        if i == '[':
            stack.append('[')
        elif i == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(']')      
        elif i == '{':
            stack.append('{')
        elif i == '}':
            if stack and stack[-1] == '{':
                stack.pop()
            else:
                stack.append('}')
        elif i == '(':
            stack.append('(')
        elif i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(')')
    return True if not stack else False
            
            