def solution(arr):
    arr.sort()
    answer = arr[0]
    for i in range(1, len(arr)):
        answer = lcd(answer, arr[i])
    return answer

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

def lcd(a, b):
    return a*b / gcd(a, b)