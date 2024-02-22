def solution(progresses, speeds):
    answer = []
    arr = list(zip(progresses, speeds))
    finish_day = []
    for p in arr:
        finish_day.append(checkFinishDay(p[0], p[1]))
    #print(finish_day)
    
    day = finish_day[0]
    finish = 1
    for i in range(1, len(finish_day)):
        if day >= finish_day[i]:
            finish += 1
        else:
            answer.append(finish)
            day = finish_day[i]
            finish = 1
    answer.append(finish)
    return answer

def checkFinishDay(progress, speed):
    day = 0
    while progress < 100:
        progress += speed
        day += 1
    return day