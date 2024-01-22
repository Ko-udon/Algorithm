def solution(picture, k):
    answer = []
    for p in picture:
        low = ''
        for pixel in p:
            low += pixel * k
        
        for _ in range(k):
            answer.append(low)
            
    return answer