def solution(s):
    answer = 0
    
    for i in range(len(s)):
        for j in range(len(s), i, -1):
            tmp = s[i:j] #i~j-1까지 슬라이싱 되므로 len(s)부터 시작, range역시 i+1까지 작동하므로 i로 설정
            if (tmp == tmp[::-1]):
                answer = max(answer, len(tmp))
    return answer