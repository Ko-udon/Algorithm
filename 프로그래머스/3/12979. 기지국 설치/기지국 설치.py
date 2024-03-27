def solution(n, stations, w):
    answer = 0
    station = w * 2 + 1
    i = 1
    
    for s in stations:
        if s - w - i > 0:
            answer += (s - w - i) // station
            if (s - w - i) % station: 
                answer += 1
        i = s + w + 1
    if n - i + 1 > 0:
        answer += (n - i + 1) // station
        if (n - i + 1) % station: 
            answer += 1
            
    return answer