import re
def solution(s):
    answer = []
    zeroCount = 0
    turnCount = 0
    while s != '1':
        zeroCount += s.count('0')
        s = re.sub('0', '', s)
        v = len(s)
        s = format(v, 'b')
        turnCount += 1
        
        
    return [turnCount, zeroCount]