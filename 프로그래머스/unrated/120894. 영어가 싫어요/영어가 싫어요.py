def solution(numbers):
    m = {'zero':'0','one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6',
        'seven':'7', 'eight':'8', 'nine':'9'}
    num = ''
    answer = ''
    
    for s in numbers:
        num += s
        if num in m:
            answer += m[num]
            num = ''
    return int(answer)